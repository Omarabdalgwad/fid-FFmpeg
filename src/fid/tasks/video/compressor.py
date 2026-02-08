import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def compress(cPath: Path, crf: int,preset: str, audio_bitrate: str):
    ffmpeg()
    ckvideo(cPath)
    compress_out= cPath.with_stem(f"{cPath.stem}_compressed")
    subprocess.run(
            ["ffmpeg", "-i", str(cPath),"-c:v", "libx264", "-crf", str(crf), "-preset",preset,"-c:a","aac","-b:a",audio_bitrate,"-y",str(compress_out),]
            , check=True,stdout=subprocess.DEVNULL)
def compress_main(app: typer.Typer):
    app.command()(compress)