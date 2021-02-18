
import youtube_dl
import sys
import os


def update():
    program = "youtube_dl"
    os.system(f"pip install -U {program}")


def wavOption(name_of_video, video):
    options = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'wav',
        # name the file the ID of the video
        'outtmpl': name_of_video+u'.%(ext)s',
        'noplaylist': True,
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video])


def mp4Option(name_of_video, video):
    options2 = {
        "format": "bestvideo+bestaudio/best",
        "videoformat": "mp4",
        "outtmpl": name_of_video+u'.%(ext)s',
        'writethumbnail': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'writesubtitles': True,
        'subtitleslangs': {'es', 'es-ES', 'es-MX'},
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            "preferedformat": "mp4",
        }]
    }
    with youtube_dl.YoutubeDL(options2) as ydl:
        ydl.download([video])
