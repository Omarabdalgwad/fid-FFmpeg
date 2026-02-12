import typer
import subprocess
from pathlib import Path
from ..initial_files.error_handling import ffmpeg , ckvideo


def info(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    ffprobe=Path(ffmpeg()).parent / "ffprobe.exe" if platform.system() == "windows" else "ffprobe"
    subprocess.run([str(ffprobe), "-v", "error", "-show_format", "-show_streams", str(cPath)], check=True)
def info_main(app: typer.Typer):
    app.command()(info)
