import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def info_main(app: typer.Typer):
    @app.command()
    def info(vid: Path):
        ffmpeg()
        ckvideo(vid)
        subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", str(vid)], check=True)