import questionary
import typer
from .denoise import denoise
#from .equalizer import equalizer
#from .compressor import compress
#from .codec import codec
#from .bitrate import bitrate
#from .channels import channels
#from .delay import delay
#from .fade import fade
#from .trim import trim
#from .replace import replace
from .mute import mute
#from .mix import mix
#from .speed import speed
#from .normalize import normalize
#from .volume import volume

def audio_main(cPath):

    while True:
        print(f"""
╔══════════════════════════════════════╗
║          AUDIO EDITING MENU          ║
╚══════════════════════════════════════╝
""")

        choice= questionary.select(
           "select the editing option you want:",
          choices=[
                "volume up/down",
                "mute audio",
                "normalize audio",
                "speed up/down",
                "decrease noise",
                "mix two audio files",
                "compress audio file",
                "equalize audio",
                "change codec",
                "change bitrate",
                "change channels",
                "add fade in/out",
                "trim audio",
                "replace audio",
                "delay audio",
                "Back to main menu",
                "exit"
            ]).ask()

        if choice is None:
            raise typer.Exit()
            
        if choice=="decrease noise":
            denoise(cPath)

        elif choice=="mute audio":
            mute(cPath)

        elif choice=="normalize audio":
            normalize(cPath)

        elif choice=="mix two audio files":
            mix(cPath)

        elif choice=="compress audio file":
            compress(cPath)

        elif choice=="equalize audio":
            equalizer(cPath)

        elif choice=="change codec":
            codec(cPath)

        elif choice=="change bitrate":
            bitrate(cPath)

        elif choice=="change channels":
            channels(cPath)

        elif choice=="add fade in/out":
            fade(cPath)

        elif choice=="trim audio":
            trim(cPath)

        elif choice=="replace audio":
            replace(cPath)

        elif choice=="delay audio":
            delay(cPath)

        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()