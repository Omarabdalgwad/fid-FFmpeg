import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def fps(cPath: Path, crf: int,preset: str, audio_bitrate: str):
    ffmpeg()
    ckvideo(cPath)
    fps_out=cPath.with_stem(f"{cPath.stem}_fps").with_suffix(".mp4")
    subprocess.run(
        [
            ffmpeg(),"-i",str(cPath),"-vf", f"fps={new_fps}",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-c:a", "copy",
            "-movflags", "+faststart",
            "-y", str(fps_out),
        ],check=True,stdout=subprocess.DEVNULL)
    
def fps_main(app: typer.Typer):
    app.command()(fps)