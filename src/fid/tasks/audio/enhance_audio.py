import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def enhance_voice(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    enhance_out=cPath.with_stem(f"{cPath.stem}_enhanced").with_suffix(cPath.suffix)
    subprocess.run(
    [
        ffmpeg(),
        "-i", str(cPath),
        "-af",
        "highpass=f=120,"
        "afftdn=nf=-38,"
        "speechnorm=e=6:r=0.0001:l=1,"
        "equalizer=f=250:g=-6,"
        "equalizer=f=3000:g=6,"
        "equalizer=f=6000:g=4,"
        "acompressor=threshold=-24dB:ratio=4:attack=5:release=300,"
        "alimiter=limit=-1.5dB",
        "-y",
        str(enhance_out),
    ],
    check=True)
def enhance_main(app:typer.Typer):
    app.command()(enhance_voice)