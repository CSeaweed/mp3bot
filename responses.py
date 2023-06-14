import downloader
import discord


async def handle(url) -> discord.File:
    path = await downloader.download(url)
    media = discord.File(path)
    return media, path

