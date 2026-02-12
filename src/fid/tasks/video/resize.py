import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def resize(cPath: Path, width: int):
    ffmpeg()
    ckvideo(cPath)
    resize_out= cPath.with_stem(f"{cPath.stem}_{width}w").with_suffix(".mp4")
    subprocess.run(
            [ffmpeg(),
                "-i", str(cPath),
                "-vf", f"scale={width}:-1",
                "-c:v", "libx264",
                "-preset", "medium",
                "-c:a", "copy",  
                "-y",
                str(resize_out)], check=True)

def resize_main(app: typer.Typer):
    app.command()(resize)
