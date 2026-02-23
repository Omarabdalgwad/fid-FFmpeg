import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo

def enhance_voice(cPath: Path):
    """
    Enhance the voice track of the given media file and write an enhanced copy next to the original.
    
    Processes the file at `cPath` with ffmpeg using a preset audio filter chain (noise reduction, speech normalization, equalization, compression, limiting) and writes the result to a new file whose stem is the original stem with "_enhanced" appended and the same suffix as the input.
    
    Parameters:
        cPath (Path): Path to the input audio or video file to enhance.
    
    Raises:
        subprocess.CalledProcessError: If the ffmpeg command fails.
    """
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
    """
    Register the enhance_voice command on a Typer application.
    
    Attach the enhance_voice function as a CLI command to the provided Typer app so the command becomes available when the app runs.
    
    Parameters:
        app (typer.Typer): Typer application to register the command on.
    """
    app.command()(enhance_voice)