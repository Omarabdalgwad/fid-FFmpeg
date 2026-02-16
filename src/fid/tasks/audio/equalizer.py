import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def equalizer(cPath: Path , F=None,W=None,G=None,band=None):
    ffmpeg()
    ckvideo(cPath)
    equalizer_out= cPath.with_stem(f"cPath.stem)_equaized")
    subprocess.run([
        ffmpeg(),"-i",str(cPath),"-af",filter_str,str(equalizer_out)], check=True)
def equalizer_main(app: typer.Typer):
    app.command()(equalizer)