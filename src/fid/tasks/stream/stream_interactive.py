import questionary
import typer
#from .hls import hls
#from .rtmp import rtmp
#from .dash import dash
#from .srt import srt
#from .udp import udp
#from .rtsp import rtsp
#from .http import http

def stream_main(cPath):

    while True:
        print(f"""
╔══════════════════════════════════════╗
║          STREAMING MENU          ║
╚══════════════════════════════════════╝
""")

        choice= questionary.select(
           "select the streaming option you want:",
          choices=[
                "stream with hls",
                "stream with rtmp",
                "stream with dash",
                "stream with srt",
                "stream with udp",
                "stream with rtsp",
                "stream with http",
                "Back to main menu",
                "exit"
            ]).ask()
            
        if choice is None:
            raise typer.Exit()
        
        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()