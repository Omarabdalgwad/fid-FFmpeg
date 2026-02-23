import requests, zipfile, platform , rich
from pathlib import Path
from tqdm import tqdm
from rich.console import Console
from time import sleep
import shutil
def ffmpeg():
    
    """
    Ensure a usable FFmpeg executable is available and return its filesystem path.
    
    Checks for an existing ffmpeg executable in the configured installation directory or on PATH. On Windows, if ffmpeg is not present the function downloads a release ZIP, extracts ffmpeg.exe into ~/.fid-ffmpeg, and returns the installed executable path. On non-Windows systems, if ffmpeg is not found on PATH the function prints an instruction to obtain FFmpeg and exits the process.
    
    Returns:
        str: Filesystem path to the ffmpeg executable.
    """
    console=Console()

    if platform.system()!= "Windows" and shutil.which("ffmpeg") is None: 
       print("Windows only is supported for ffmpeg installation")
       print("pleaze download ffmpeg from https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip")
       exit()

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
    if not cPath.exists() or not cPath.is_file() or cPath.suffix.lower() not in [".mp4",".avi",".mkv",".mov",".flv",".wmv",".webm"]:  
        print("incorrect video path or unsupported video fromat")
        exit()