import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def resize_main(app: typer.Typer):
    @app.command()
    def resize(video_path: Path, width: int):
        ffmpeg()
        ckvideo(video_path)
        resize_out= video_path.with_stem(f"{video_path.stem}_{width}w").with_suffix(".mp4")
        subprocess.run(
            ["ffmpeg",
                "-i", str(video_path),
                "-vf", f"scale={width}:-1",
                "-c:v", "libx264",
                "-preset", "medium",
                "-c:a", "copy",  
                "-y",
                str(resize_out)], check=True)