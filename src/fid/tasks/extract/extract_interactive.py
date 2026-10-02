import questionary
import typer
from .audio import audio
from .frames import frames

def extract_main(cPath):

    while True:
        print(f"""
╔══════════════════════════════════════╗
║          EXTRACTING MENU          ║
╚══════════════════════════════════════╝
""")

        choice= questionary.select(
           "select the editing option you want:",
          choices=[
                "extract frames",
                "extract audio",
                "Back to main menu",
                "exit"
            ]).ask()
        if choice is None:
            raise typer.Exit()

        if choice=="extract audio":
           audio(cPath)

        elif choice=="extract frames":
            frames(cPath)

        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()