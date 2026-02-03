import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def frames_main(app: typer.Typer):
    @app.command()
    def frames(video_path: Path):
        ffmpeg()
        ckvideo(video_path)
        Fdir= video_path.parent
        frames_out= Fdir / "Frames" / video_path.stem
        frames_out.mkdir(parents=True,exist_ok=True)
        subprocess.run(["ffmpeg", "-i", str(video_path),str(frames_out/ "frame_%02d.png")],check=True )