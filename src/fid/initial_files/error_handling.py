import requests, zipfile, platform , rich
from pathlib import Path
from tqdm import tqdm
from rich.console import Console
from time import sleep
import shutil
import sys
def ffmpeg():
    
    """
    Ensure a usable FFmpeg executable is available and return its filesystem path.
    
    On Windows, downloads and installs ffmpeg.exe into ~/.fid-ffmpeg if not already present; on non-Windows systems, verifies ffmpeg is available on PATH and prints instructions and exits if it is not found.
    
    Returns:
        str: Filesystem path to the ffmpeg executable.
    """
    console=Console()

    if platform.system()!= "Windows" and shutil.which("ffmpeg") is None: 
       print("Windows only is supported for ffmpeg installation")
       print("pleaze download ffmpeg from https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
       sys.exit(1)

    FFmpeg_installation= Path.home()/".fid-ffmpeg"
    FFmpeg_installation.mkdir(exist_ok=True)
    zip=FFmpeg_installation/"ffmpeg.zip"
    exe=FFmpeg_installation/"ffmpeg.exe"
    
    with console.status("checking for ffmpeg....") as status:
        sleep(2)
        if exe.exists():
            print("ffmpeg already exists")
            return str(exe)
        elif shutil.which("ffmpeg") is not None: 
            print("ffmpeg already exists")
            return shutil.which("ffmpeg")
        else:
            print("\nFFmpeg not found , Downloading it....\n")

    r =requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip",stream=True)
    total = int(r.headers.get("content-length"))
    with open(zip,"wb")as f:
         with tqdm(total=total,unit="B",unit_scale=True,colour="green", bar_format="{l_bar}{bar} | {n_fmt}/{total_fmt}" ) as bar:
            for chunk in r.iter_content(1024*1024):
                f.write(chunk)
                bar.update(len(chunk))
    with console.status("extracting....") as status:
        sleep(1.5)
        with zipfile.ZipFile(zip)as z:
            for name in z.namelist():
                if name.endswith("ffmpeg.exe"):
                   extract= z.extract(name , FFmpeg_installation)
                   Path(extract).rename(exe)
                   print("ffmpeg installed .")
                   break
    return str(exe)

def ckvideo(cPath):
    """
    Check that `cPath` points to an existing video file with a supported extension.
    
    If `cPath` does not exist, is not a file, or its suffix (case-insensitive) is not one of: .mp4, .avi, .mkv, .mov, .flv, .wmv, .webm, the function prints an error message and exits the process.
    
    Parameters:
        cPath (Path): Path-like object referencing the candidate video file.
    """
    if not cPath.exists() or not cPath.is_file() or cPath.suffix.lower() not in [".mp4",".avi",".mkv",".mov",".flv",".wmv",".webm"]:  
        print("incorrect video path or unsupported video fromat")
        sys.exit(1)
