import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def gif_main(app: typer.Typer):
    @app.command()
    def gif(vid: Path):
        ffmpeg()
        ckvideo(vid)
        gif_out=vid.with_suffix(".gif")
        subprocess.run(["ffmpeg", "-i", str(vid), "-t", "3", "-vf", "scale=320:-1", "-y", str(gif_out)], check=True)