import questionary
import typer
from .compressor import compress
#from .concat import concat
#from .crop import crop
from .fps import fps
from .gif import gif
from .resize import resize
from .rotate import rotate
#from .speed import speed
#from .trim import trim


def video_main(cPath):

    while True:
        print(f"""
╔══════════════════════════════════════╗
║          VIDEO EDITING MENU          ║
╚══════════════════════════════════════╝
""")
        choice= questionary.select(
           "select the editing option you want:",
          choices=[
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
            ]).ask()

        if choice is None:
            raise typer.Exit()
            
        if choice=="compress the video":
            compress_choice = questionary.select(
                "Choose compression option:",
                choices=[
                    "smallest size",
                    "medium size (recommended)",
                    "high quality",
                    "Back to main menu",
                    "exit"
                ]
                ).ask()

            if compress_choice is None:
                raise typer.Exit()
            if compress_choice == "Back to main menu":
                continue
            if compress_choice == "exit":
                raise typer.Exit()

            if compress_choice == "smallest size": 
               compress(cPath, crf=33, preset="slower", audio_bitrate="64k")
            elif compress_choice == "medium size (recommended)":
                compress(cPath, crf=27, preset="medium", audio_bitrate="96k")
            elif compress_choice == "high quality":
                compress(cPath, crf=21, preset="medium", audio_bitrate="128k")
     
        elif choice=="make gif":
            gif(cPath)
        
        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()