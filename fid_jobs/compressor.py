import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def compress_main(app: typer.Typer):
    @app.command()
    def compress(vid: Path, crf: int=28):
        ffmpeg()
        ckvideo(vid)
        compress_out= vid.with_stem(f"{vid.stem}_compressed").with_suffix(".mkv")
        subprocess.run(["ffmpeg", "-i", str(vid),"-c:v", "libx264", "-crf", str(crf), "-preset","medium","-c:a","aac","-b:a","96k","-y",str(compress_out),], check=True)