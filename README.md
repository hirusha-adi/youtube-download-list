
# YouTube Video and Playlist Downloader

This Python script allows you to download YouTube videos, playlists, and even search for videos with ease. It offers a command-line interface to specify the type of download, video quality, and source.

## Usage

### Download Videos, Playlists, and Channels

```bash
python3 ytdll.py <download_type> <quality> <file>
```

- `<download_type>`: Choose the type of content to download.
  - `v`: Video
  - `p`: Playlist
  - `c`: Channel

- `<quality>`: Specify the download quality.
  - Video Quality:
    - `2160p` (4K)
    - `1440p`
    - `1080p`
    - `720p`
    - `480p`
    - `360p`
    - `240p`
    - `144p`
  - Audio Quality:
    - `32kbps`
    - `64kbps`
    - `128kbps`
    - `192kbps`
    - `240kbps`
    - `256kbps`
    - `320kbps`

- `<file>`: Provide a text file containing YouTube video or playlist links.

### Search for Videos

```bash
python3 ytdll.py s <quality> <video_name>
```

- `<quality>`: Specify the download quality as described above.
- `<video_name>`: Enter the name of the video you want to search for and download.

## Platform Compatibility

The script is compatible with both Windows and non-Windows systems. It detects your platform automatically.

## Requirements

- Python 3
- [pytube](https://pypi.org/project/pytube/)
- [youtubesearchpython](https://pypi.org/project/youtubesearchpython/)

Install the required packages using the following commands:

```bash
pip install pytube
pip install youtubesearchpython
```

## Example Usages

### Download a Video

```bash
python3 ytdll.py v 720p video_links.txt
```

### Download a Playlist

```bash
python3 ytdll.py p 1080p playlist_links.txt
```

### Search and Download a Video

```bash
python3 ytdll.py s 360p "Halsey Not Afraid Anymore"
```
