import questionary
import typer
from .audio import audio
from .frames import frames
from .thumbnails import thumbnails
from .keyframes import keyframes
from .audio_track import audio_track
from .audio_channels import audio_channels
from .subtitles import subtitles
from .subtitles_track import subtitles_track
from .subtitles_convert import subtitles_convert
from .chapters import chapters
from .attachments import attachments

def video_main(video_path):

    while True:
        choice= questionary.select(
           "select the editing option you want:",
          choices=[
                "extract frames",
                "extract audio",
                "extract subtitles",
                "extract chapters",
                "extract thumbnails",
                "extract keyframes",
                "extract audio_track",
                "extract audio_channels",
                "extract subtitles_track",
                "subtitles_converter",
                "extract attachments",
                "Back to main menue",
                "exit"
            ]).ask()
        if choice=="extract audio":
           audio(video_path)

        elif choice=="extract frames":
            frames(video_path)

        elif choice=="extract subtitles":
            subtitles(video_path)

        elif choice=="extract chapters":
            chapters(video_path)

        elif choice=="extract thumbnails":
            thumbnails(video_path)

        elif choice=="extract keyframes":
            keyframes(video_path)

        elif choice=="extract audio_track":
            audio_track(video_path)

        elif choice=="extract audio_channels":
            audio_channels(video_path)

        elif choice=="extract subtitles_track":
            subtitles_track(video_path)

        elif choice=="subtitles_converter":
            subtitles_convert(video_path)

        elif choice=="extract attachments":
            attachments(video_path)

        elif choice=="Back to main menue":
            return

        elif choice=="exit":
           raise typer.Exit()