import typer
import subprocess
from pathlib import Path
import shutil

def ffmpeg():
    if shutil.which("ffmpeg")is None:
       print("ffmpeg isn't installed\n download from: https://ffmpeg.org/download.html")
       raise typer.Exit()

def ckvideo(vid:Path):
    if not vid.exists():
     print("file doesn't exist :)")
     raise typer.Exit()