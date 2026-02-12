import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def frames(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    Fdir= cPath.parent
    frames_out= Fdir / "Frames" / cPath.stem
    frames_out.mkdir(parents=True,exist_ok=True)
    subprocess.run([ffmpeg(), "-i", str(cPath),str(frames_out/ "frame_%02d.png")],check=True )
def frames_main(app: typer.Typer):
    app.command()(frames)
