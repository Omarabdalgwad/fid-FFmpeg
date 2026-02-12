import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def denoise(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    denoise_out= cPath.with_stem(f"{cPath.stem}_denoise")
    subprocess.run([ffmpeg(),"-i",str(cPath),"-af","afftdn",str(denoise_out)],check=True)

def denoise_main(app: typer.Typer):
    app.command()(denoise)