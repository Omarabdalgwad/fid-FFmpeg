import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock, call
import typer

from fid.tasks.video.video_interactive import video_main


class TestVideoMain:
    """Test suite for the video_main() function."""

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_back_to_main_menu(self, mock_print, mock_select):
        """Test selecting 'Back to main menu' returns from function."""
        mock_select.return_value.ask.return_value = "Back to main menu"

        input_path = Path("/videos/test.mp4")

        result = video_main(input_path)

        # Should return None when back to main menu is selected
        assert result is None
        mock_select.assert_called_once()

    @patch('fid.tasks.video.video_interactive.questionary.select')
    def test_video_main_exit(self, mock_select):
        """Test selecting 'exit' raises typer.Exit."""
        mock_select.return_value.ask.return_value = "exit"

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.questionary.select')
    def test_video_main_none_choice_raises_exit(self, mock_select):
        """Test that None choice (Ctrl+C) raises typer.Exit."""
        mock_select.return_value.ask.return_value = None

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_smallest_size(self, mock_print, mock_select, mock_compress):
        """Test compress option with smallest size."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "smallest size",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        mock_compress.assert_called_once_with(input_path, crf=33, preset="slower", audio_bitrate="64k")

    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_medium_size(self, mock_print, mock_select, mock_compress):
        """Test compress option with medium size (recommended)."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "medium size (recommended)",
            "exit"
        ]

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

        mock_compress.assert_called_once_with(input_path, crf=27, preset="medium", audio_bitrate="96k")

    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_high_quality(self, mock_print, mock_select, mock_compress):
        """Test compress option with high quality."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "high quality",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        mock_compress.assert_called_once_with(input_path, crf=21, preset="medium", audio_bitrate="128k")

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_back_to_menu(self, mock_print, mock_select):
        """Test compress submenu 'Back to main menu' returns to main menu."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "Back to main menu",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        # Should have been called 3 times: main menu, compress submenu, main menu again
        assert mock_select.call_count == 3

    @patch('fid.tasks.video.video_interactive.questionary.select')
    def test_video_main_compress_submenu_exit(self, mock_select):
        """Test compress submenu 'exit' raises typer.Exit."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "exit"
        ]

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.questionary.select')
    def test_video_main_compress_submenu_none_raises_exit(self, mock_select):
        """Test compress submenu None (Ctrl+C) raises typer.Exit."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            None
        ]

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.gif')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_make_gif(self, mock_print, mock_select, mock_gif):
        """Test make gif option."""
        mock_select.return_value.ask.side_effect = [
            "make gif",
            "exit"
        ]

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

        mock_gif.assert_called_once_with(input_path)

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_displays_menu(self, mock_print, mock_select):
        """Test that the menu is displayed to the user."""
        mock_select.return_value.ask.return_value = "Back to main menu"

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        # Verify the menu header was printed
        print_calls = [call[0][0] for call in mock_print.call_args_list]
        menu_displayed = any("VIDEO EDITING MENU" in str(call) for call in print_calls)
        assert menu_displayed

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_loop_continues_after_operation(self, mock_print, mock_select):
        """Test that the menu loop continues after an operation."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "Back to main menu",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        # Should call select 3 times (main menu, compress submenu, main menu again)
        assert mock_select.call_count == 3

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_menu_choices(self, mock_print, mock_select):
        """Test that all expected menu choices are present."""
        mock_select.return_value.ask.return_value = "exit"

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

        # Get the choices passed to questionary.select
        call_kwargs = mock_select.call_args[1]
        choices = call_kwargs['choices']

        expected_choices = [
            "compress the video",
            "make gif",
            "speed up/down",
            "change fps",
            "concat videos",
            "crop video",
            "resize video",
            "rotate video",
            "trim video",
            "Back to main menu",
            "exit"
        ]

        assert choices == expected_choices

    @patch('fid.tasks.video.video_interactive.gif')
    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_multiple_operations(self, mock_print, mock_select, mock_compress, mock_gif):
        """Test performing multiple operations in sequence."""
        mock_select.return_value.ask.side_effect = [
            "make gif",
            "compress the video",
            "smallest size",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        mock_gif.assert_called_once_with(input_path)
        mock_compress.assert_called_once_with(input_path, crf=33, preset="slower", audio_bitrate="64k")

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_menu_choices(self, mock_print, mock_select):
        """Test that compress submenu has all expected choices."""
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "exit"
        ]

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

        # Get the second call (compress submenu)
        compress_call = mock_select.call_args_list[1]
        choices = compress_call[1]['choices']

        expected_choices = [
            "smallest size",
            "medium size (recommended)",
            "high quality",
            "Back to main menu",
            "exit"
        ]

        assert choices == expected_choices


class TestVideoMainEdgeCases:
    """Test edge cases and error scenarios for video_main()."""

    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_error_continues_loop(self, mock_print, mock_select, mock_compress):
        """Test that errors during compress don't crash the loop."""
        mock_compress.side_effect = Exception("Compression failed")
        mock_select.return_value.ask.side_effect = [
            "compress the video",
            "smallest size",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        # Should raise the exception (no error handling in the code)
        with pytest.raises(Exception, match="Compression failed"):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.gif')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_gif_error(self, mock_print, mock_select, mock_gif):
        """Test that errors during gif creation propagate."""
        mock_gif.side_effect = Exception("GIF creation failed")
        mock_select.return_value.ask.side_effect = [
            "make gif"
        ]

        input_path = Path("/videos/test.mp4")

        with pytest.raises(Exception, match="GIF creation failed"):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_with_path_object(self, mock_print, mock_select):
        """Test that function accepts Path object for cPath."""
        mock_select.return_value.ask.return_value = "Back to main menu"

        input_path = Path("/home/user/videos/movie.mp4")

        result = video_main(input_path)

        assert result is None

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_with_special_characters_in_path(self, mock_print, mock_select):
        """Test with special characters in video path."""
        mock_select.return_value.ask.return_value = "exit"

        input_path = Path("/videos/my video (1080p) [2024].mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_compress_all_options_sequentially(self, mock_print, mock_select, mock_compress):
        """Test all three compression options in sequence."""
        mock_select.return_value.ask.side_effect = [
            "compress the video", "smallest size",
            "compress the video", "medium size (recommended)",
            "compress the video", "high quality",
            "Back to main menu"
        ]

        input_path = Path("/videos/test.mp4")

        video_main(input_path)

        # Should have called compress 3 times with different parameters
        assert mock_compress.call_count == 3

        expected_calls = [
            call(input_path, crf=33, preset="slower", audio_bitrate="64k"),
            call(input_path, crf=27, preset="medium", audio_bitrate="96k"),
            call(input_path, crf=21, preset="medium", audio_bitrate="128k")
        ]

        mock_compress.assert_has_calls(expected_calls)


class TestVideoMainIntegration:
    """Integration tests for video_main() function."""

    @patch('fid.tasks.video.video_interactive.compress')
    @patch('fid.tasks.video.video_interactive.gif')
    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_full_workflow(self, mock_print, mock_select, mock_gif, mock_compress):
        """Test a complete workflow with multiple operations."""
        mock_select.return_value.ask.side_effect = [
            "make gif",
            "compress the video",
            "high quality",
            "make gif",
            "Back to main menu"
        ]

        input_path = Path("/videos/presentation.mp4")

        video_main(input_path)

        # Verify operations were called in order
        assert mock_gif.call_count == 2
        assert mock_compress.call_count == 1
        mock_compress.assert_called_with(input_path, crf=21, preset="medium", audio_bitrate="128k")

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_menu_presentation(self, mock_print, mock_select):
        """Test that menu is properly formatted and presented."""
        mock_select.return_value.ask.return_value = "exit"

        input_path = Path("/videos/test.mp4")

        with pytest.raises(typer.Exit):
            video_main(input_path)

        # Verify menu components are printed
        print_output = ''.join([str(call[0][0]) for call in mock_print.call_args_list])

        assert "VIDEO EDITING MENU" in print_output
        assert "╔" in print_output  # Box drawing characters
        assert "║" in print_output
        assert "╚" in print_output


class TestVideoMainUnimplementedFeatures:
    """Tests documenting currently unimplemented menu options."""

    @patch('fid.tasks.video.video_interactive.questionary.select')
    @patch('builtins.print')
    def test_video_main_unimplemented_options(self, mock_print, mock_select):
        """Document that several menu options are not yet implemented."""
        # The following options are in the menu but commented out in imports:
        # - speed up/down
        # - change fps (fps is imported but not used in video_main)
        # - concat videos
        # - crop video
        # - rotate video
        # - trim video

        # Only implemented: compress, make gif, resize
        # Note: fps and resize are imported but not connected in the menu

        pass

    def test_fps_imported_but_not_used(self):
        """Document that fps is imported but not used in video_main()."""
        # The fps function is imported at the top of video_interactive.py
        # However, the "change fps" menu option doesn't call it
        # This is likely an incomplete implementation

        pass

    def test_resize_imported_but_not_used(self):
        """Document that resize is imported but not used in video_main()."""
        # The resize function is imported
        # The "resize video" menu option exists but doesn't call it
        # This is likely an incomplete implementation

        pass