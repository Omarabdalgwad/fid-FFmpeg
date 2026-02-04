import typer
import subprocess
from pathlib import Path
from ..initial_files.error_handling import ffmpeg , ckvideo


def info(video_path: Path):
    ffmpeg()
    ckvideo(cPath)
    subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", str(video_path)], check=True)
def info_main(app: typer.Typer):
    app.command()(info)