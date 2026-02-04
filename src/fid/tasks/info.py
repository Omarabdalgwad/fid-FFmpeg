import typer
import subprocess
from pathlib import Path
from ..initial_files.error_handling import ffmpeg , ckvideo


def info(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    subprocess.run(["ffprobe", "-v", "error", "-show_format", "-show_streams", str(cPath)], check=True)
def info_main(app: typer.Typer):
    app.command()(info)
