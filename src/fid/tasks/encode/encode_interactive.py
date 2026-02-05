
import questionary
import typer
#from .h264 import h264
#from .h265 import h265
#from .av1 import av1

def encode_main(cPath):

    while True:
        print(f"""
╔══════════════════════════════════════╗
║          ENCODING MENU          ║
╚══════════════════════════════════════╝
""")

        choice= questionary.select(
           "select the encoding option you want:",
          choices=[
                "encode to h264",
                "encode to h265",
                "encode to av1",
                "Back to main menu",
                "exit"
            ]).ask()
        if choice is None:
            raise typer.Exit()
            
       
        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()