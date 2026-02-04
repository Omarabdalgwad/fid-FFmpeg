import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def gif(video_path: Path):
    ffmpeg()
    ckvideo(video_path)
    gif_out=video_path.with_suffix(".gif")
    subprocess.run(["ffmpeg", "-i", str(video_path), "-t", "3", "-vf", "scale=320:-1", "-y", str(gif_out)], check=True)

def gif_main(app: typer.Typer):
    app.command()(gif)
