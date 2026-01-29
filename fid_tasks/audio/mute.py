import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def mute_main(app: typer.Typer):
    @app.command()
    def mute(vid: Path):
        ffmpeg()
        ckvideo(vid)
        mute_out=vid.with_stem(f"{vid.stem}_muted").with_suffix(vid.suffix)
        subprocess.run(["ffmpeg", "-i", str(vid), "-c", "copy", "-an", "-y", str(mute_out)], check=True)