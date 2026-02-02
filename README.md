# fid-ffmpeg [![PyPI Downloads](https://static.pepy.tech/personalized-badge/fid-ffmpeg?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/fid-ffmpeg)

ffmpeg based cli for video operations 
```bash
fid
```
https://github.com/user-attachments/assets/abcc8aa0-3ada-4548-8f99-987687cfccd9

- you need to install python >=3.9 : [Download Python](https://www.python.org/downloads/)
- install ffmpeg : [Download FFmpeg](https://www.ffmpeg.org/download.html)
- then install fid-cli with pip :
```bash
pip install fid-ffmpeg
```
## installation demo
https://github.com/user-attachments/assets/6063b46b-dd4a-4cb3-a318-869f37bcf60f

## Commands
| Command | Description |
|---------|------------|
| `fid --help` | show help for fid cli |
| `fid info "videoPath"` | `to know all info about the video` |
| `fid audio "videoPath"` | `extract audio from the video` |
| `fid mute "videoPath"` | `mute the video` |
| `fid gif "videoPath"` | `make a gif from the video` |
| `fid frames "videoPath"` | `extract all video frames and add them in a folder`|
| `fid frames "videoPath"` | `extract all video frames and add them in a folder`|
| `fid compress "videoPath"` | `Compress the video to reduce its file size`|


```
```

FID
├─ LICENSE
├─ pyproject.toml
├─ README.md
└─ src
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