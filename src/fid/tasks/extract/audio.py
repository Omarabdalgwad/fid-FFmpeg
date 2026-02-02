import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def audio_main(app: typer.Typer):
    @app.command()
    def audio(video_path: Path):
        ffmpeg()
        ckvideo(video_path)
        audio_out=video_path.with_suffix(".mp3")
        subprocess.run(["ffmpeg", "-i", str(video_path), "-vn", "-acodec", "libmp3lame", "-y", str(audio_out)], check=True)