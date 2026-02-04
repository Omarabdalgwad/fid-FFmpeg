import typer
from pathlib import Path
import shutil

def ffmpeg():
    if shutil.which("ffmpeg")is None:
       print("ffmpeg isn't installed\n download from: https://ffmpeg.org/download.html")
       raise typer.Exit()

def ckvideo(video_path:Path):
    path_str = Path(video_path)
    if not path_str.exists():
       print("file doesn't exist :)")
       raise typer.Exit()