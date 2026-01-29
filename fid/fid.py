import typer
from .welcome import welcome
from ..fid_tasks.extract.audio import audio_main
from ..fid_tasks.extract.frames import frames_main
from ..fid_tasks.audio.mute import mute_main
from ..fid_tasks.video.compressor import compress_main
from ..fid_tasks.video.gif import gif_main
from ..fid_tasks.info import info_main


app= typer.Typer()

@app.callback(invoke_without_command=True)
def start(ctx : typer.Context):
    if ctx.invoked_subcommand is None:
        welcome()


audio_main(app)
compress_main(app)
frames_main(app)
gif_main(app)
info_main(app)
mute_main(app)

if __name__=="__main__":
        app()