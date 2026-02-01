import questionary
import typer
from .h264 import h264
from .h265 import h265
from .av1 import av1

def encode_main(video_path):

    while True:
        choice= questionary.select(
           "select the encoding option you want:",
          choices=[
                "encode to h264",
                "encode to h265",
                "encode to av1"
                "Back to main menue",
                "exit"
            ]).ask()
        if choice=="encode to h264":
          h264(video_path)

        elif choice=="encode to h265":
            h265(video_path)

        elif choice=="encode to av1":
            av1(video_path)

        elif choice=="Back to main menue":
            return

        elif choice=="exit":
           raise typer.Exit()