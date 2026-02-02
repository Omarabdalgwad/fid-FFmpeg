from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

def welcome():
    ascii=pyfiglet.figlet_format("fid-ffmpeg",font="bloody")
    logo = Text(ascii)
    logo.stylize("bold gradient(cyan, magenta)")
    console.print(logo, justify="center")
    content =(
        "[bold]fid-ffmpeg Helper[/bold]\n\n"
        "[green]Commands:[/green]\n"
        " • info     Show video info\n"
        " • audio    Extract audio\n"
        " • frames   Extract frames\n"
        " • gif      Create gif\n"
        " • mute     Remove audio\n"
        " • compress Compress video\n\n"
        "[dim]Run : fid <command> <video path>[/dim]")
    console.print(Panel(content,title="v0.5.0",border_style="bright_blue",expand=False),justify="center")