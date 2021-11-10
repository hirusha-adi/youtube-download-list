__version__ = "0.1"
__author__ = "ZeaCeR#5641"

import os
import platform
import sys

from pytube import *
from youtubesearchpython import VideosSearch


if platform.system().lower().startswith('win'):
    CLEAR = "cls"
    PIP = "pip"
    PYTHON = "python"
else:
    CLEAR = "clear"
    PIP = "pip3"
    PYTHON = "python3"


def ARG_ERROR():
    print("""
Usage:
python3 ytdll.py v 144p README.md
    """)


def YTDLLF_ERROR():
    print("""
An error occured while downloading
    """)


# Download Type
try:
    first_opt = str(sys.argv[1])
    if first_opt.lower().startswith('p'):
        print("+ Download type: Playlist")
        download_type = "playlist"
    elif first_opt.lower().startswith('c'):
        print("+ Download type: Channel")
        download_type = "channel"
    else:
        print("+ Download type: Video")
        download_type = "video"
except:
    ARG_ERROR()
    sys.exit()

# Video Quality + Video or Audio
try:
    second_opt = str(sys.argv[2])
    if second_opt.lower() == '2160p':
        print("+ Download quality: 2160p/4K")
        dl_quality = '2160p'
    elif second_opt.lower() == '1440p':
        print("+ Download quality: 1440p")
        dl_quality = '1440p'
    elif second_opt.lower() == '1080p':
        print("+ Download quality: 1080p")
        dl_quality = '1080p'
    elif second_opt.lower() == '1080p':
        print("+ Download quality: 1080p")
        dl_quality = '1080p'
    elif second_opt.lower() == '720p':
        print("+ Download quality: 720p")
        dl_quality = '720p'
    elif second_opt.lower() == '480p':
        print("+ Download quality: 480p")
        dl_quality = '480p'
    elif second_opt.lower() == '360p':
        print("+ Download quality: 360p")
        dl_quality = '360p'
    elif second_opt.lower() == '240p':
        print("+ Download quality: 240p")
        dl_quality = '240p'
    elif second_opt.lower() == '144p':
        print("+ Download quality: 144p")
        dl_quality = '144p'
    elif second_opt.lower() == '32kbps':
        print("+ Download quality: 32kbps")
        dl_quality = '32kbps'
    elif second_opt.lower() == '64kbps':
        print("+ Download quality: 64kbps")
        dl_quality = '64kbps'
    elif second_opt.lower() == '128kbps':
        print("+ Download quality: 128kbps")
        dl_quality = '128kbps'
    elif second_opt.lower() == '192kbps':
        print("+ Download quality: 192kbps")
        dl_quality = '192kbps'
    elif second_opt.lower() == '240kbps':
        print("+ Download quality: 240kbps")
        dl_quality = '240kbps'
    elif second_opt.lower() == '256kbps':
        print("+ Download quality: 256kbps")
        dl_quality = '256kbps'
    elif second_opt.lower() == '320kbps':
        print("+ Download quality: 320kbps")
        dl_quality = '320kbps'
    else:
        print("+ Download quality: 720p")
        dl_quality = '720p'
except:
    ARG_ERROR()
    sys.exit()

# Download links list file
try:
    third_option = str(sys.argv[3])
    if os.path.exists(third_option) == False:
        ARG_ERROR()
    else:
        with open(f"""{third_option}""", "r", encoding="utf-8") as file:
            all_file_lines = list(line for line in (l.strip()
                                  for l in file) if line)
except:
    ARG_ERROR()
    sys.exit()


def DOWNLOAD_VIDEO(qualityvid: str, urlvid: str):
    all_audio_qualities_tup = ("32kbps", "64kbps", "128kbps",
                               "160kbps", "192kbps", "240kbps", "256kbps", "320kbps")
    try:
        yt = YouTube(urlvid)
    except Exception as e:
        print("Error", e)
        YTDLLF_ERROR()
        sys.exit()  # not sure i want to keep it here... idk

    video_name_corrected = f"""{yt.title.replace('|', 'x').replace('?', 'x').replace('>', 'x').replace('<', 'x').replace(':', 'x').replace(';', 'x').replace('"', 'x').replace("'", 'x')}"""
    print(f"* Trying to downlod {video_name_corrected} in {qualityvid}")

    # Audio
    if qualityvid in all_audio_qualities_tup:
        try:
            video = yt.streams.filter(only_audio=True).filter(
                abr=f"{qualityvid}").first().download()
            print(f"+ DONE: {video}")
        except:
            try:
                print(
                    f"* Trying to downlod {video_name_corrected} in highet available quality")
                video = yt.streams.filter(only_audio=True).first().download()
                print(f"+ DONE: {video}")
            except:
                print(
                    f"* Trying to downlod {video_name_corrected} in lowest available quality")
                video = yt.streams.filter(only_audio=True).last().download()
                print(f"+ DONE: {video}")

    # Video
    else:
        try:
            video = yt.streams.filter(res=f"{qualityvid}").filter(
                progressive=True).first().download()
            print(f"+ DONE: {video}")
        except:
            try:
                print(
                    f"* Trying to downlod {video_name_corrected} in highet available quality")
                video = yt.streams.filter(
                    progressive=True).get_highest_resolution().download()
                print(f"+ DONE: {video}")
            except:
                print(
                    f"* Trying to downlod {video_name_corrected} in lowest available quality")
                video = yt.streams.filter(
                    progressive=True).get_lowest_resolution().download()
                print(f"+ DONE: {video}")


def ENTIRE_PROGRAM():
    global download_type
    if download_type == "playlist":
        for one_line in all_file_lines:
            pl = Playlist(f'{one_line}')
            for one_url in pl.video_urls:
                DOWNLOAD_VIDEO(qualityvid=dl_quality, urlvid=one_url)
    elif download_type == "channel":
        for one_line in all_file_lines:
            cl = Channel(f'{one_line}')
            for one_url in cl.video_urls:
                DOWNLOAD_VIDEO(qualityvid=dl_quality, urlvid=one_url)
    else:
        for one_line in all_file_lines:
            DOWNLOAD_VIDEO(qualityvid=dl_quality, urlvid=one_line)


ENTIRE_PROGRAM()
