import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def enhance_voice(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    enhance_out=cPath.with_stem(f"{cPath.stem}_enhanced").with_suffix(cPath.suffix)
    subprocess.run([ffmpeg(),"-i",str(cPath),"-af","afftdn,equalizer=f=3000:t=q:w=1:g=5","-y",str(enhance_out)],check=True)
def enhance_main(app:typer.Typer):
    app.command()(enhance_voice)