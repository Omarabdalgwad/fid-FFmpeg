import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg, ckvideo


def equalizer(cPath: Path, frequency: int = 1000, gain: int = 0):
    ffmpeg()
    ckvideo(cPath)
    equalizer_out = cPath.with_stem(f"{cPath.stem}_equalized").with_suffix(cPath.suffix)
    subprocess.run([
        ffmpeg(),
        "-i", str(cPath),
        "-af", f"equalizer=f={frequency}:g={gain}",
        "-y",
        str(equalizer_out)
    ], check=True)

def equalizer_main(app: typer.Typer):
    app.command()(equalizer)