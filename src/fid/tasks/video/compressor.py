import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def compress(video_path: Path, crf: int=28):
    ffmpeg()
    ckvideo(video_path)
    compress_out= video_path.with_stem(f"{video_path.stem}_compressed").with_suffix(".mkv")
    subprocess.run(
            ["ffmpeg", "-i", str(video_path),"-c:v", "libx264", "-crf", str(crf), "-preset","medium","-c:a","aac","-b:a","96k","-y",str(compress_out),]
            , check=True)
def compress_main(app: typer.Typer):
    app.command()(compress)