# fid-ffmpeg [![PyPI Downloads](https://static.pepy.tech/personalized-badge/fid-ffmpeg?period=total&units=international_system&left_color=black&right_color=green&left_text=downloads)](https://pepy.tech/project/fid-ffmpeg)

Python wrapper around the FFmpeg command line tool for video operations.

```bash
fid
```
https://github.com/user-attachments/assets/abcc8aa0-3ada-4548-8f99-987687cfccd9

## Requirements
- python >=3.9 : [Download Python](https://www.python.org/downloads/)
- ffmpeg : [Download FFmpeg](https://www.ffmpeg.org/download.html)
- install fid-cli with pip :
```bash
pip install fid-ffmpeg
```
## installation demo
https://github.com/user-attachments/assets/6063b46b-dd4a-4cb3-a318-869f37bcf60f

## Usage
Run `fid` for the interactive menu, or use direct commands:

- `fid --help`: Show help for fid CLI.
- `fid info "videoPath"`: Get all info about the video.
- `fid audio "videoPath"`: Extract audio from the video.
- `fid mute "videoPath"`: Mute the video.
- `fid gif "videoPath"`: Create a GIF from the video.
- `fid frames "videoPath"`: Extract all video frames into a folder.
- `fid compress "videoPath"`: Compress the video to reduce file size.

For more advanced options, use the interactive mode by running `fid` without arguments.

## Features
- Interactive CLI with menus for video, audio, extract, stream, and encode operations.
- Built with Typer for commands and Questionary for interactive prompts.
- Rich console output for a modern look.

## Project Structure



```

FID
├─ LICENSE
├─ pyproject.toml
├─ README.md
└─ src/
   fid/
   ├─ fid.py
   ├─ fid_interactive.py
   ├─ initial_files
   │  ├─ error_handling.py
   │  └─ __init__.py
   ├─ tasks
   │  ├─ audio
   │  │  ├─ audio_interactive.py
   │  │  ├─ bitrate.py
   │  │  ├─ channels.py
   │  │  ├─ codec.py
   │  │  ├─ compressor.py
   │  │  ├─ delay.py
   │  │  ├─ denoise.py
   │  │  ├─ equalizer.py
   │  │  ├─ fade.py
   │  │  ├─ mix.py
   │  │  ├─ mute.py
   │  │  ├─ normalize.py
   │  │  ├─ replace.py
   │  │  ├─ speed.py
   │  │  ├─ trim.py
   │  │  ├─ volume.py
   │  │  └─ __init__.py
   │  ├─ encode
   │  │  ├─ av1.py
   │  │  ├─ encode_interactive.py
   │  │  ├─ h264.py
   │  │  ├─ h265.py
   │  │  └─ __init__.py
   │  ├─ extract
   │  │  ├─ attachments.py
   │  │  ├─ audio.py
   │  │  ├─ audio_channels.py
   │  │  ├─ audio_track.py
   │  │  ├─ chapters.py
   │  │  ├─ extract_interactive.py
   │  │  ├─ frames.py
   │  │  ├─ keyframes.py
   │  │  ├─ subtitles.py
   │  │  ├─ subtitles_convert.py
   │  │  ├─ subtitles_track.py
   │  │  ├─ thumbnails.py
   │  │  └─ __init__.py
   │  ├─ info.py
   │  ├─ stream
   │  │  ├─ dash.py
   │  │  ├─ hls.py
   │  │  ├─ http.py
   │  │  ├─ rtmp.py
   │  │  ├─ rtsp.py
   │  │  ├─ srt.py
   │  │  ├─ stream_interactive.py
   │  │  ├─ udp.py
   │  │  └─ __init__.py
   │  ├─ video
   │  │  ├─ compressor.py
   │  │  ├─ concat.py
   │  │  ├─ crop.py
   │  │  ├─ fps.py
   │  │  ├─ gif.py
   │  │  ├─ resize.py
   │  │  ├─ rotate.py
   │  │  ├─ speed.py
   │  │  ├─ trim.py
   │  │  ├─ video_interactive.py
   │  │  └─ __init__.py
   │  └─ __init__.py
   ├─ welcome.py
   └─ __init__.py

```

## Contributing
Contributions are welcome! Fork the repo, create a branch, and submit a pull request. For major changes, open an issue first.

## About
Python wrapper around the FFmpeg command line tool.

[PyPI Project](https://pypi.org/project/fid-ffmpeg/)

### Topics
- audio
- python
- cli
- video
- ffmpeg
- frames
- gif
- compressor
- ffmpeg-wrapper
- rich
- mute
- typer-cli
