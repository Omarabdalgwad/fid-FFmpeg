import questionary
import typer
from .compressor import compress
#from .concat import concat
#from .crop import crop
#from .fps import fps
from .gif import gif
#from .resize import resize
#from .rotate import rotate
#from .speed import speed
#from .trim import trim

def video_main(cPath):

    while True:
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
           compress(cPath)
     
        elif choice=="make gif":
            gif(cPath)
        
        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()