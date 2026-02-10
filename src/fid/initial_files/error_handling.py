import requests
from pathlib import Path
from tqdm import tqdm
import platform
import typer

def ffmpeg():
    folder = Path("ffmpeg")
    folder.mkdir(exist_ok=True) 
    if platform.system() == "Windows":
       url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials/ffmpeg.exe"
       exe = "ffmpeg.exe"

    exe_path= folder / exe
    if exe_path.exists(): 
        print("FFmpeg is installed")
        return exe_path

    print("Downloading FFmpeg....\n")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total= int(r.headers.get("content-length", 0))
        with open(exe_path,"wb") as f,tqdm(total=total,unit="B",unit_scale=True) as bar:
            for chunk in r.iter_content(1024):
                f.write(chunk)
                bar.update(len(chunk))


def ckvideo(cPath):
    if not cPath.exists():  # لو الفيديو مش موجود يخرج
        print("this video doesn't exist")
        raise typer.Exit()