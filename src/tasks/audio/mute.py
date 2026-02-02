import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def mute_main(app: typer.Typer):
    @app.command()
    def mute(video_path: Path):
        ffmpeg()
        ckvideo(video_path)
        mute_out=vid.with_stem(f"{video_path.stem}_muted").with_suffix(video_path.suffix)
        subprocess.run(["ffmpeg", "-i", str(video_path), "-c", "copy", "-an", "-y", str(mute_out)], check=True)