import questionary
import typer
from .tasks.audio.audio_interactive import audio_main
from .tasks.encode.encode_interactive import encode_main
from .tasks.extract.extract_interactive import extract_main
from .tasks.stream.stream_interactive import stream_main
from .tasks.video.video_interactive import video_main

def fid_main(video_path):

    while True:
        choice= questionary.select(
           "select the editing option you want:",
          choices=[
                "video editing",
                "audio editing",
                "extract from the video",
                "streaming options",
                "encoding options",
                "exit"
            ]).ask()
        if choice=="video editing":
          video_main(video_path)

        elif choice=="audio editing":
            audio_main(video_path)
        
        elif choice=="extract from the video":
            extract_main(video_path)

        elif choice=="streaming options":
            stream_main(video_path)
        
        elif choice=="encoding options":
            encode_main(video_path)

        elif choice=="exit":
           raise typer.Exit()