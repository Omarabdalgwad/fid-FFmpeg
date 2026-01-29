import typer
import subprocess
from pathlib import Path
from .error_handling import ffmpeg , ckvideo

def audio_main(app: typer.Typer):
    @app.command()
    def audio(vid: Path):
        ffmpeg()
        ckvideo(vid)
        audio_out=vid.with_suffix(".mp3")
        subprocess.run(["ffmpeg", "-i", str(vid), "-vn", "-acodec", "libmp3lame", "-y", str(audio_out)], check=True)