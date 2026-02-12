import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def mute(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    mute_out=cPath.with_stem(f"{cPath.stem}_muted").with_suffix(cPath.suffix)
    subprocess.run([ffmpeg(), "-i", str(cPath), "-c", "copy", "-an", "-y", str(mute_out)], check=True)

def mute_main(app: typer.Typer):
    app.command()(mute)
