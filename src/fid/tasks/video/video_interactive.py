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

def video_main(video_path):

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
           compress(video_path)
     
        elif choice=="make gif":
            gif(video_path)
        
        
        
        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()