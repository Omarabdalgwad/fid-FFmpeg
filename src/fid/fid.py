import typer
import questionary
from pathlib import Path
from .ui import ui
from .fid_interactive import fid_main
from .tasks.extract.audio import audio_main
from .tasks.extract.frames import frames_main
from .tasks.audio.mute import mute_main
from .tasks.video.compressor import compress_main
from .tasks.video.gif import gif_main
from .tasks.info import info_main
from .initial_files.error_handling import ffmpeg

app= typer.Typer()

@app.callback(invoke_without_command=True)
def start(ctx : typer.Context):
    if ctx.invoked_subcommand is not None:
        return
       
    ffmpeg()    
    ui() 

    while True:
        video_path= questionary.path("enter the path to your video:").ask()
        if video_path is None:
            raise typer.Exit()

        cPath= Path(video_path.strip('"').strip("'").replace("\\","/"))
        if cPath.is_file():
            fid_main(cPath)
            break
        else:
            print(f" '{video_path}' is not a valid file path. Please try again") 

audio_main(app)
compress_main(app)
frames_main(app)
gif_main(app)
info_main(app)
mute_main(app)

if __name__=="__main__":
        app()