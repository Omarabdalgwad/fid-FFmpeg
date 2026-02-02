import questionary
import typer
from .denoise import denoise
from .equalizer import equalizer
from .compressor import compress
from .codec import codec
from .bitrate import bitrate
from .channels import channels
from .delay import delay
from .fade import fade
from .trim import trim
from .replace import replace
from .mute import mute
from .mix import mix
from .speed import speed
from .normalize import normalize
from .volume import volume

def audio_main(video_path):

    while True:
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
        if choice==  "volume up/down":
          volume(video_path)

        elif choice=="mute audio":
            mute(video_path)

        elif choice=="speed up/down":
            speed(video_path)

        elif choice=="normalize audio":
            normalize(video_path)

        elif choice=="decrease noise":
            denoise(video_path)

        elif choice=="mix two audio files":
            mix(video_path)

        elif choice=="compress audio file":
            compress(video_path)

        elif choice=="equalize audio":
            equalizer(video_path)

        elif choice=="change codec":
            codec(video_path)

        elif choice=="change bitrate":
            bitrate(video_path)

        elif choice=="change channels":
            channels(video_path)

        elif choice=="add fade in/out":
            fade(video_path)

        elif choice=="trim audio":
            trim(video_path)

        elif choice=="replace audio":
            replace(video_path)

        elif choice=="delay audio":
            delay(video_path)

        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()