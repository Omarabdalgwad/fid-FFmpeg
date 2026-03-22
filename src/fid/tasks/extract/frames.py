import typer
import subprocess
from pathlib import Path
from rich.console import Console
from ...initial_files.error_handling import ffmpeg, ckvideo

console=Console()

def frames(cPath: Path):
    ffmpeg()
    ckvideo(cPath)
    Fdir= cPath.parent
    frames_out= Fdir / "Frames" / cPath.stem
    frames_out.mkdir(parents=True,exist_ok=True)
    
    with console.status("[green]Extracting frames...."):
      subprocess.run([ffmpeg(), "-i", str(cPath),str(frames_out/ "frame_%02d.png")],stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL, check=True )
    console.print("[green] Frames extracted successfully[/green]")

def frames_main(app: typer.Typer):
    app.command()(frames)