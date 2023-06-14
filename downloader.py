from pytube import YouTube
import pathlib


async def fix_suffix(media: str, original: str, new: str):
    to_fix: pathlib.WindowsPath = pathlib.Path(media)
    print(to_fix)
    to_fix.rename(media.replace(original, new))
    return media.replace(original, new)

async def download(url: str):
    print(url)
    video = YouTube(url)
    media = video.streams.filter(only_audio=True).first()
    media = media.download("./cache")
    media = await fix_suffix(media, "mp4", "mp3")
    return media
