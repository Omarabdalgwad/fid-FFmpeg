import questionary
import typer
from .hls import hls
from .rtmp import rtmp
from .dash import dash
from .srt import srt
from .udp import udp
from .rtsp import rtsp
from .http import http

def stream_main(video_path):

    while True:
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

        if choice=="stream with hls":
           hls(video_path)

        elif choice=="stream with rtmp":
            rtmp(video_path)

        elif choice=="stream with dash":
            dash(video_path)
        
        elif choice=="stream with srt":
            srt(video_path)
        
        elif choice=="stream with udp":
            udp(video_path)
        
        elif choice=="stream with rtsp":
            rtsp(video_path)
        
        elif choice=="stream with http":
            http(video_path)

        elif choice=="Back to main menu":
            return

        elif choice=="exit":
           raise typer.Exit()