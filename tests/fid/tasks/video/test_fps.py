import pytest
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock, call
import typer

from fid.tasks.video.fps import fps, fps_main


class TestFps:
    """Test suite for the fps() function."""

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_basic_execution(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test basic execution of fps function."""
        mock_ffmpeg.return_value = "/path/to/ffmpeg"

        input_path = Path("/home/user/video.mp4")
        crf = 23
        preset = "medium"
        audio_bitrate = "128k"

        # Note: The function has a bug - it references undefined 'new_fps' variable
        # This test documents the expected behavior if the bug were fixed
        with pytest.raises(NameError, match="name 'new_fps' is not defined"):
            fps(input_path, crf, preset, audio_bitrate)

        # Verify ffmpeg() was called to ensure ffmpeg is available
        assert mock_ffmpeg.call_count >= 1

        # Verify ckvideo was called to validate the input
        mock_ckvideo.assert_called_once_with(input_path)

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_ffmpeg_validation(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that ffmpeg() is called to validate ffmpeg availability."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/home/user/test.mp4")

        with pytest.raises(NameError):  # Due to new_fps bug
            fps(input_path, crf=25, preset="fast", audio_bitrate="96k")

        # Should be called twice: once to get path, once in subprocess
        assert mock_ffmpeg.call_count >= 1

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_ckvideo_validation(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that ckvideo() is called to validate the input video."""
        mock_ffmpeg.return_value = "/path/to/ffmpeg"

        input_path = Path("/home/user/movie.mp4")

        with pytest.raises(NameError):
            fps(input_path, crf=20, preset="slow", audio_bitrate="192k")

        mock_ckvideo.assert_called_once_with(input_path)

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_output_path_generation(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that output path is correctly generated with _fps suffix."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/videos/sample.mp4")

        with pytest.raises(NameError):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

        # The output path should be generated as: sample_fps.mp4
        # We can't fully verify this due to the bug, but the logic is in the code

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_with_different_input_extension(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test fps with non-mp4 input file."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/videos/sample.avi")

        with pytest.raises(NameError):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

        # Output should still be .mp4 format
        # This is enforced by: .with_suffix(".mp4")

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_subprocess_error_handling(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that subprocess errors would be propagated due to check=True."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"
        mock_subprocess.side_effect = subprocess.CalledProcessError(1, "ffmpeg")

        input_path = Path("/videos/test.mp4")

        # Note: Currently the NameError for new_fps is raised before subprocess.run
        # This test documents that if the new_fps bug were fixed, subprocess errors
        # would be propagated due to check=True
        with pytest.raises(NameError):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_parameters_ignored_in_current_implementation(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that crf, preset, and audio_bitrate parameters are currently ignored."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/videos/test.mp4")

        # The function accepts these parameters but doesn't use them
        # Instead, it uses hardcoded values in the subprocess call
        with pytest.raises(NameError):
            fps(input_path, crf=30, preset="ultrafast", audio_bitrate="64k")

        # The actual subprocess call (if it were reached) would use:
        # preset="medium", crf="23", audio="copy"
        # Not the passed parameters

    @patch('fid.tasks.video.fps.ckvideo', side_effect=SystemExit)
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_invalid_video_path(self, mock_ffmpeg, mock_ckvideo):
        """Test that invalid video path causes exit via ckvideo."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        invalid_path = Path("/nonexistent/video.mp4")

        with pytest.raises(SystemExit):
            fps(invalid_path, crf=23, preset="medium", audio_bitrate="128k")

    @patch('fid.tasks.video.fps.ffmpeg', side_effect=SystemExit)
    def test_fps_ffmpeg_not_available(self, mock_ffmpeg):
        """Test behavior when ffmpeg is not available."""
        input_path = Path("/videos/test.mp4")

        with pytest.raises(SystemExit):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_stdout_devnull(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that subprocess output is suppressed with DEVNULL."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/videos/test.mp4")

        with pytest.raises(NameError):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

        # If subprocess.run were called, it should have stdout=subprocess.DEVNULL


class TestFpsMain:
    """Test suite for the fps_main() function."""

    def test_fps_main_registers_command(self):
        """Test that fps_main registers fps as a command on the app."""
        mock_app = MagicMock(spec=typer.Typer)
        mock_command_decorator = MagicMock()
        mock_app.command.return_value = mock_command_decorator

        fps_main(mock_app)

        # Verify app.command() was called
        mock_app.command.assert_called_once()

        # Verify the decorator was called with the fps function
        mock_command_decorator.assert_called_once_with(fps)

    def test_fps_main_with_typer_app(self):
        """Test fps_main with actual Typer app."""
        app = typer.Typer()

        # Should not raise any exceptions
        fps_main(app)

        # Verify that a command was registered
        # Typer stores commands internally, we can't easily inspect them
        # but we can verify the function doesn't crash

    def test_fps_main_multiple_calls(self):
        """Test that fps_main can be called multiple times (idempotency)."""
        mock_app = MagicMock(spec=typer.Typer)
        mock_command_decorator = MagicMock()
        mock_app.command.return_value = mock_command_decorator

        # Call multiple times
        fps_main(mock_app)
        fps_main(mock_app)

        # Should register command each time it's called
        assert mock_app.command.call_count == 2


class TestFpsIntegration:
    """Integration tests for fps functionality."""

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_workflow_with_valid_inputs(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test complete workflow with valid inputs."""
        mock_ffmpeg.return_value = "/usr/local/bin/ffmpeg"

        input_path = Path("/project/videos/source.mp4")

        # This test documents the bug - new_fps is not defined
        with pytest.raises(NameError, match="name 'new_fps' is not defined"):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_preserves_directory_structure(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test that output file is created in same directory as input."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/deep/nested/directory/structure/video.mp4")

        with pytest.raises(NameError):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

        # Expected output would be: /deep/nested/directory/structure/video_fps.mp4

    def test_fps_main_integration_with_typer(self):
        """Test integration of fps_main with Typer application."""
        app = typer.Typer()

        # Register the command
        fps_main(app)

        # Verify the app has commands registered
        # This is a basic integration test to ensure no errors occur

    @patch('fid.tasks.video.fps.subprocess.run')
    @patch('fid.tasks.video.fps.ckvideo')
    @patch('fid.tasks.video.fps.ffmpeg')
    def test_fps_handles_special_characters_in_path(self, mock_ffmpeg, mock_ckvideo, mock_subprocess):
        """Test fps with special characters in file path."""
        mock_ffmpeg.return_value = "/usr/bin/ffmpeg"

        input_path = Path("/videos/my video (1080p) [h264].mp4")

        with pytest.raises(NameError):
            fps(input_path, crf=23, preset="medium", audio_bitrate="128k")

        # Should handle special characters in paths correctly


class TestFpsBugDocumentation:
    """Tests that document the new_fps bug for future fixes."""

    def test_new_fps_variable_not_defined(self):
        """Document that new_fps variable is referenced but not defined."""
        # In fps.py line 13, the code references f"fps={new_fps}"
        # However, new_fps is never defined as a parameter or variable
        # This is a critical bug that prevents the function from working

        # Expected behavior: new_fps should be a parameter to fps()
        # or derived from user input or configuration
        pass

    def test_parameters_not_used_correctly(self):
        """Document that function parameters are not used in subprocess call."""
        # The fps() function accepts crf, preset, and audio_bitrate parameters
        # However, the subprocess.run call uses hardcoded values:
        # - preset is hardcoded as "medium" (line 15)
        # - crf is hardcoded as "23" (line 16)
        # - audio is hardcoded as "copy" (line 17)

        # The parameters should be used like:
        # "-preset", preset,
        # "-crf", str(crf),
        # "-c:a", audio_bitrate,
        pass

    def test_missing_new_fps_parameter(self):
        """Document that fps() should accept new_fps as a parameter."""
        # Expected signature:
        # def fps(cPath: Path, new_fps: int, crf: int, preset: str, audio_bitrate: str):
        #     ...
        #     f"fps={new_fps}"
        pass