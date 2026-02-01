import questionary
import typer
from ..fid_tasks.audio import audio_interactive.audio_main
from ..fid_tasks.audio import encode_interactive.encode_main
from ..fid_tasks.audio import extract_interactive.extract_main
from ..fid_tasks.audio import stream_interactive.stream_main
from ..fid_tasks.audio import video_interactive.video_main

def fid_main(video_path):

    while True:
        choice= questionary.select(
           "select the editing option you want:",
          choices=[
                "video editing",
                "audio editing",
                "extract from media",
                "straming options",
                "encoding options",
                "exit"
            ]).ask()
        if choice=="video editing":
          video_main(video_path)

        elif choice=="audio editing":
            audio_main(video_path)
        
        elif choice=="extract from the video":
            extract_main(video_path)

        elif choice=="straming options":
            stream_main(video_path)
        
        elif choice=="encoding options":
            encode_main(video_path)

        elif choice=="exit":
           raise typer.Exit()