import requests
import zipfile
import platform
import shutil
import sys
from pathlib import Path
from time import sleep
from tqdm import tqdm
from rich.console import Console


def ffmpeg():
    console = Console()
    FFmpeg_installation = Path.home() / ".fid-ffmpeg"
    FFmpeg_installation.mkdir(exist_ok=True)
    zip_path = FFmpeg_installation / "ffmpeg.zip"
    exe = FFmpeg_installation / "ffmpeg.exe"

    if shutil.which("ffmpeg") is not None:
        print("ffmpeg already exists in system")
        return shutil.which("ffmpeg")

    if exe.exists():
        print("ffmpeg already exists")
        return str(exe)

    print("\nFFmpeg not found, downloading it...\n")

    try:
        r =requests.get(
            "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",
            stream=True,
            timeout=30,
        )
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error downloading FFmpeg: {e}")
        print("Please download it manually from:")
        print("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
        sys.exit(1)
    total = int(r.headers.get("content-length", 0))

    try:
        with open(zip_path, "wb") as f:
            with tqdm(
                total=total,
                unit="B",
                unit_scale=True,
                colour="green",
                bar_format="{l_bar}{bar} | {n_fmt}/{total_fmt}",
            ) as bar:
                for chunk in r.iter_content(1024 * 1024):
                    f.write(chunk)
                    bar.update(len(chunk))
    except Exception as e:
        print(f"Error saving FFmpeg: {e}")
        sys.exit(1)

    with console.status("extracting...."):
        sleep(1.5)
        try:
            with zipfile.ZipFile(zip_path) as z:
                for name in z.namelist():
                    if name.endswith("ffmpeg.exe"):
                        extract = z.extract(name, FFmpeg_installation)
                        Path(extract).rename(exe)
                        print("ffmpeg installed!")
                        break
        except zipfile.BadZipFile:
            print("Error: Downloaded file is corrupted")
            sys.exit(1)

    zip_path.unlink(missing_ok=True)

    return str(exe)


def ckvideo(cPath):
    if not cPath.exists() or not cPath.is_file():
        print("incorrect video path")
        sys.exit(1)

    supported = [".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv", ".webm"]
    if cPath.suffix.lower() not in supported:
        print("unsupported video format")
        sys.exit(1)