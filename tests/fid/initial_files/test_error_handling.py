import pytest
import platform
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock, mock_open, call
from io import BytesIO

from fid.initial_files.error_handling import ffmpeg, ckvideo


class TestFFmpeg:
    """Test suite for the ffmpeg() function."""

    @patch('fid.initial_files.error_handling.platform.system')
    @patch('fid.initial_files.error_handling.shutil.which')
    @patch('builtins.print')
    def test_ffmpeg_non_windows_no_ffmpeg_exits(self, mock_print, mock_which, mock_system):
        """Test that non-Windows systems without ffmpeg exit with instructions."""
        mock_system.return_value = "Linux"
        mock_which.return_value = None

        with pytest.raises(SystemExit):
            ffmpeg()

        mock_print.assert_any_call("Windows only is supported for ffmpeg installation")
        mock_print.assert_any_call("pleaze download ffmpeg from https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")

    @patch('fid.initial_files.error_handling.platform.system')
    @patch('fid.initial_files.error_handling.shutil.which')
    @patch('fid.initial_files.error_handling.sleep')
    @patch('builtins.print')
    def test_ffmpeg_existing_exe_windows(self, mock_print, mock_sleep, mock_which, mock_system):
        """Test that existing ffmpeg.exe is found and returned on Windows."""
        mock_system.return_value = "Windows"
        mock_which.return_value = None

        # Create a temporary directory for testing
        from tempfile import TemporaryDirectory
        import os

        with TemporaryDirectory() as tmpdir:
            # Create ffmpeg.exe file
            ffmpeg_dir = Path(tmpdir) / ".fid-ffmpeg"
            ffmpeg_dir.mkdir(exist_ok=True)
            ffmpeg_exe = ffmpeg_dir / "ffmpeg.exe"
            ffmpeg_exe.touch()

            with patch('fid.initial_files.error_handling.Path.home', return_value=Path(tmpdir)):
                result = ffmpeg()

                # Should return the path to existing exe
                assert result == str(ffmpeg_exe)
                mock_print.assert_called_with("ffmpeg already exists")

    @patch('fid.initial_files.error_handling.platform.system')
    @patch('fid.initial_files.error_handling.shutil.which')
    @patch('fid.initial_files.error_handling.sleep')
    @patch('builtins.print')
    def test_ffmpeg_existing_in_path(self, mock_print, mock_sleep, mock_which, mock_system):
        """Test that ffmpeg in PATH is found and returned."""
        mock_system.return_value = "Windows"
        mock_which.return_value = "/usr/bin/ffmpeg"

        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            # Don't create ffmpeg.exe, so it will use the one from PATH
            with patch('fid.initial_files.error_handling.Path.home', return_value=Path(tmpdir)):
                result = ffmpeg()

                assert result == "/usr/bin/ffmpeg"
                mock_print.assert_called_with("ffmpeg already exists")

    @patch('fid.initial_files.error_handling.platform.system')
    @patch('fid.initial_files.error_handling.shutil.which')
    @patch('fid.initial_files.error_handling.requests.get')
    @patch('fid.initial_files.error_handling.zipfile.ZipFile')
    @patch('fid.initial_files.error_handling.sleep')
    @patch('builtins.print')
    def test_ffmpeg_download_and_install(self, mock_print, mock_sleep,
                                         mock_zipfile, mock_requests_get,
                                         mock_which, mock_system):
        """Test downloading and installing ffmpeg when not found."""
        mock_system.return_value = "Windows"
        mock_which.return_value = None

        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            ffmpeg_dir = Path(tmpdir) / ".fid-ffmpeg"
            zip_file = ffmpeg_dir / "ffmpeg.zip"
            exe_file = ffmpeg_dir / "ffmpeg.exe"

            # Setup requests mock
            mock_response = MagicMock()
            mock_response.headers.get.return_value = "1000000"
            mock_response.iter_content.return_value = [b"chunk1", b"chunk2"]
            mock_requests_get.return_value = mock_response

            # Setup zipfile mock
            mock_zip = MagicMock()
            mock_zip.namelist.return_value = ["ffmpeg-release-essentials/bin/ffmpeg.exe", "other_file.txt"]

            # Create the extracted file when extract is called
            def mock_extract(name, path):
                extracted = Path(path) / name
                extracted.parent.mkdir(parents=True, exist_ok=True)
                extracted.touch()
                return str(extracted)

            mock_zip.extract.side_effect = mock_extract
            mock_zipfile.return_value.__enter__.return_value = mock_zip

            with patch('fid.initial_files.error_handling.Path.home', return_value=Path(tmpdir)):
                result = ffmpeg()

            # Verify download was initiated
            mock_requests_get.assert_called_once_with(
                "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",
                stream=True
            )

            # Result should be a string path to ffmpeg.exe
            assert isinstance(result, str)
            assert result.endswith("ffmpeg.exe")

    @patch('fid.initial_files.error_handling.platform.system')
    @patch('fid.initial_files.error_handling.shutil.which')
    @patch('fid.initial_files.error_handling.sleep')
    @patch('builtins.print')
    def test_ffmpeg_non_windows_with_ffmpeg_in_path(self, mock_print, mock_sleep, mock_which, mock_system):
        """Test non-Windows system with ffmpeg available in PATH."""
        mock_system.return_value = "Linux"
        mock_which.return_value = "/usr/bin/ffmpeg"

        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as tmpdir:
            with patch('fid.initial_files.error_handling.Path.home', return_value=Path(tmpdir)):
                result = ffmpeg()

        assert result == "/usr/bin/ffmpeg"
        mock_print.assert_called_with("ffmpeg already exists")


class TestCkvideo:
    """Test suite for the ckvideo() function."""

    def test_ckvideo_valid_mp4(self):
        """Test that a valid mp4 file passes validation."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".mp4"

        # Should not raise or exit
        try:
            ckvideo(mock_path)
        except SystemExit:
            pytest.fail("ckvideo() should not exit for valid mp4 file")

    def test_ckvideo_valid_avi(self):
        """Test that a valid avi file passes validation."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".avi"

        try:
            ckvideo(mock_path)
        except SystemExit:
            pytest.fail("ckvideo() should not exit for valid avi file")

    def test_ckvideo_valid_mkv(self):
        """Test that a valid mkv file passes validation."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".mkv"

        try:
            ckvideo(mock_path)
        except SystemExit:
            pytest.fail("ckvideo() should not exit for valid mkv file")

    def test_ckvideo_all_supported_formats(self):
        """Test all supported video formats pass validation."""
        supported_formats = [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm"]

        for fmt in supported_formats:
            mock_path = MagicMock(spec=Path)
            mock_path.exists.return_value = True
            mock_path.is_file.return_value = True
            mock_path.suffix.lower.return_value = fmt

            try:
                ckvideo(mock_path)
            except SystemExit:
                pytest.fail(f"ckvideo() should not exit for valid {fmt} file")

    @patch('builtins.print')
    def test_ckvideo_nonexistent_file(self, mock_print):
        """Test that a nonexistent file causes exit."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = False
        mock_path.is_file.return_value = False
        mock_path.suffix.lower.return_value = ".mp4"

        with pytest.raises(SystemExit):
            ckvideo(mock_path)

        mock_print.assert_called_with("incorrect video path or unsupported video fromat")

    @patch('builtins.print')
    def test_ckvideo_not_a_file(self, mock_print):
        """Test that a directory causes exit."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = False
        mock_path.suffix.lower.return_value = ".mp4"

        with pytest.raises(SystemExit):
            ckvideo(mock_path)

        mock_print.assert_called_with("incorrect video path or unsupported video fromat")

    @patch('builtins.print')
    def test_ckvideo_unsupported_format(self, mock_print):
        """Test that an unsupported file format causes exit."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".txt"

        with pytest.raises(SystemExit):
            ckvideo(mock_path)

        mock_print.assert_called_with("incorrect video path or unsupported video fromat")

    @patch('builtins.print')
    def test_ckvideo_uppercase_extension(self, mock_print):
        """Test that uppercase extensions are handled correctly."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".mp4"
        mock_path.suffix = ".MP4"

        # Should not raise since .lower() is called
        try:
            ckvideo(mock_path)
        except SystemExit:
            pytest.fail("ckvideo() should handle uppercase extensions")

    @patch('builtins.print')
    def test_ckvideo_mixed_case_extension(self, mock_print):
        """Test that mixed case extensions are handled correctly."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".avi"
        mock_path.suffix = ".AvI"

        try:
            ckvideo(mock_path)
        except SystemExit:
            pytest.fail("ckvideo() should handle mixed case extensions")

    @patch('builtins.print')
    def test_ckvideo_no_extension(self, mock_print):
        """Test that a file with no extension causes exit."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ""

        with pytest.raises(SystemExit):
            ckvideo(mock_path)

        mock_print.assert_called_with("incorrect video path or unsupported video fromat")

    @patch('builtins.print')
    def test_ckvideo_double_extension(self, mock_print):
        """Test file with double extension like video.backup.mp4."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".mp4"

        try:
            ckvideo(mock_path)
        except SystemExit:
            pytest.fail("ckvideo() should handle files with double extensions")

    @patch('builtins.print')
    def test_ckvideo_edge_case_nearly_supported_format(self, mock_print):
        """Test that similar but unsupported formats are rejected."""
        mock_path = MagicMock(spec=Path)
        mock_path.exists.return_value = True
        mock_path.is_file.return_value = True
        mock_path.suffix.lower.return_value = ".mp3"  # audio, not video

        with pytest.raises(SystemExit):
            ckvideo(mock_path)

        mock_print.assert_called_with("incorrect video path or unsupported video fromat")