import typer
import subprocess
from pathlib import Path
from ...initial_files.error_handling import ffmpeg , ckvideo


def compress(cPath: Path, crf: int,preset: str, audio_bitrate: str):
    
    ckvideo(cPath)
    compress_out= cPath.with_stem(f"{cPath.stem}_compressed").with_suffix(".mp4")
    subprocess.run(
            [str(ffmpeg()), "-i", str(cPath),"-c:v", "libx265", "-crf", str(crf), "-preset", preset,"-vf", "hqdn3d=1.5:1.5:6:6,eq=contrast=1.05:brightness=0.01:saturation=1.05","-pix_fmt","yuv420p","-tag:v", "hvc1","-c:a","aac","-b:a",audio_bitrate,"-movflags", "+faststart","-y",str(compress_out),]
            , check=True,stdout=subprocess.DEVNULL)
def compress_main(app: typer.Typer):
    app.command()(compress)