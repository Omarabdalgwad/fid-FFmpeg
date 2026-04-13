import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def gif(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    gif_out=cPath.with_suffix(".gif")
    subprocess.run([ffmpeg(), "-i", str(cPath), "-t", "3", "-vf", "scale=320:-1", "-y", str(gif_out)], check=True)

def gif_main(app: typer.Typer):
    app.command()(gif)