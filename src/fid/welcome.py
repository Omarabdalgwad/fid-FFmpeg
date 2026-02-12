from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.align import Align
from rich import box
import pyfiglet

console = Console()

def welcome():
    ascii = pyfiglet.figlet_format("fid-ffmpeg", font="slant")
    console.print(Text(ascii, style="green bold"))
    video_panel = Panel(
        "- Compress video\n"
        "- Create GIF\n",title="Video Options",border_style="green",box=box.ROUNDED,)
    audio_panel = Panel(
        "- Extract audio\n"
        "- Normalize audio\n"
        "- Noise reduction",
        title="Audio Options",
        border_style="green",
        box=box.ROUNDED,)
    stream_panel = Panel(
        "Coming Soon",
        title="Stream Options",
        border_style="green",
        box=box.ROUNDED,)
    extra_panel = Panel(
        "- Extract frames\n"
        "- Extract audio",
        title="Extra Options",
        border_style="green",
        box=box.ROUNDED,)
    encode_panel = Panel(
        "Coming Soon",
        title="Encode Options",
        border_style="green",
        box=box.ROUNDED,)
    capcut_panel = Panel(
        "[bold]Enhance Audio[/bold]\n"
        " Noise reduction\n",title="CapCut Pro",border_style="white",box=box.ROUNDED,)

    left_grid = Table.grid(padding=(1, 2))
    left_grid.add_row(video_panel, audio_panel)
    left_grid.add_row(extra_panel, stream_panel)
    left_grid.add_row(encode_panel, "")
    interactive = Panel(left_grid,title="Interactive Options",border_style="dim",box=box.DOUBLE,padding=(1, 2),)
    main_layout = Table.grid(padding=(2, 4))
    main_layout.add_row(interactive, Align.center(capcut_panel))
    console.print(Align.left(main_layout))
    console.print(Align.left(Panel("Usage: fid <input_file>",border_style="dim",)))