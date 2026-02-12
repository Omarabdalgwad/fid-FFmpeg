import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def normalize(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    normalize_out=cPath.with_stem(f"{cPath.stem}_normalized").with_suffix(cPath.suffix)
    subprocess.run([ffmpeg(),"-i",str(cPath),"-af","loudnorm","-y",str(normalize_out)],check=True)

def normalized_main(app:typer.Typer):
    app.command()(normalize)