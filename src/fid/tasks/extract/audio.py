import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def audio(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    audio_out=cPath.with_suffix(".mp3")
    subprocess.run([ffmpeg(), "-i", str(cPath), "-vn", "-acodec", "libmp3lame", "-y", str(audio_out)], check=True)
def audio_main(app: typer.Typer):
    app.command()(audio)
