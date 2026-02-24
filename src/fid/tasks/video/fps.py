import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def fps(cPath: Path, crf: int,preset: str, audio_bitrate: str):
    """
    Re-encode the given video to an MP4 file with a changed frame rate and save it alongside the source.
    
    The output is written to a file named "<original_stem>_fps.mp4" next to the input and will overwrite an existing file with that name. The function invokes ffmpeg to perform the re-encoding and preserves the input audio stream.
    
    Parameters:
        cPath (Path): Path to the source video file.
        crf (int): Target constant rate factor for the encoder (controls quality; lower is higher quality).
        preset (str): Encoding preset to trade off compression efficiency for speed (e.g., "fast", "medium", "slow").
        audio_bitrate (str): Target audio bitrate (e.g., "128k") for the output audio stream.
    """
    ffmpeg()
    ckvideo(cPath)
    fps_out=cPath.with_stem(f"{cPath.stem}_fps").with_suffix(".mp4")
    subprocess.run(
        [
            ffmpeg(),"-i",str(cPath),"-vf", f"fps={new_fps}",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-c:a", "copy",
            "-movflags", "+faststart",
            "-y", str(fps_out),
        ],check=True,stdout=subprocess.DEVNULL)
    
def fps_main(app: typer.Typer):
    """
    Register the `fps` command on the provided Typer application.
    
    Parameters:
        app (typer.Typer): Typer application instance to which the `fps` command will be added.
    """
    app.command()(fps)