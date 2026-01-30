import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def info_main(app: typer.Typer):
    @app.command()
    def info(video_path: Path):
        ffmpeg()
        ckvideo(video_path)
        subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", str(video_path)], check=True)