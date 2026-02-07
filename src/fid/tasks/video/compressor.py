import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def compress(cPath: Path, crf: int=28):
    ffmpeg()
    ckvideo(cPath)
    compress_out= cPath.with_stem(f"{cPath.stem}_compressed").with_suffix(".mkv")
    subprocess.run(
            ["ffmpeg", "-i", str(cPath),"-c:v", "libx264", "-crf", str(crf), "-preset","medium","-c:a","aac","-b:a","96k","-y",str(compress_out),]
            , check=True)
def compress_main(app: typer.Typer):
    app.command()(compress)