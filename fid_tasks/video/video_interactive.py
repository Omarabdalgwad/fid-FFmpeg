import questionary
import typer
from .compressor import compress
from .concat import concat
from .crop import crop
from .fps import fps
from .gif import gif
from .resize import resize
from .rotate import rotate
from .speed import speed
from .trim import trim

def video_main(video_path):

    while True:
        choice= questionary.select(
           "select the editing option you want:",
          choices=[
                "compress the video",
                "make gif",
                "speed up/down",
                "change fbs",
                "concat videos",
                "crop video",
                "resize video",
                "rotate video",
                "trim video",
                "Back to main menue",
                "exit"
            ]).ask()
        if choice=="compress the video":
          compress(video_path)

        elif choice=="make gif":
            gif(video_path)

        elif choice=="speed up/down":
            speed(video_path)

        elif choice=="change fbs":
            fps(video_path)

        elif choice=="concat videos":
            concat(video_path)

        elif choice=="crop video":
            crop(video_path)

        elif choice=="resize video":
            resize(video_path)

        elif choice=="rotate video":
            rotate(video_path)

        elif choice=="trim video":
            trim(video_path)

        elif choice=="Back to main menue":
            return

        elif choice=="exit":
           raise typer.Exit()