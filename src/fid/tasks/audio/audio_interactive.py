import questionary
import typer
from .denoise import denoise
from .equalizer import equalizer
from .mute import mute
from .enhance_audio import enhance_voice

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
                "enhance voice",
                "mute audio",
                "decrease noise",
                "Back to main menu",
                "exit"
            ]).ask()

        if choice is None:
            raise typer.Exit()
  
        if choice=="decrease noise":
            denoise(cPath)
        elif choice=="enhance voice":
            enhance_voice(cPath)
        elif choice=="mute audio":
            mute(cPath)
        elif choice=="Back to main menu":
            return
        elif choice=="exit":
           raise typer.Exit()