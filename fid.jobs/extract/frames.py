import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def frames_main(app: typer.Typer):
    @app.command()
    def frames(vid: Path):
        ffmpeg()
        ckvideo(vid)
        Fdir= vid.parent
        frames_out= Fdir / "Frames" / vid.stem
        frames_out.mkdir(parents=True,exist_ok=True)
        subprocess.run(["ffmpeg", "-i", str(vid),str(frames_out/ "frame_%02d.png")],check=True )
   