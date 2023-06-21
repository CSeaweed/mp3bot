import discord
from discord import app_commands
from discord.ext import commands 
import responses
import json
import pathlib
import os
from logger import write_to_history


def build_mention(id: str) -> str:
    return f"<@{id}>"

def get_secrets(secret: str) -> dict:
    secrets: dict = {}
    with open(secret, encoding="utf-8", mode="r") as data:
        secrets = json.load(data)
    return secrets

def run_bot():
    secret_file = "./secrets.json"
    SECRETS: dict = get_secrets(secret_file)    
    
    TOKEN, INV = SECRETS["TOKEN"], SECRETS["INV"]
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='!', intents=intents)
        
    @client.event
    async def on_ready():
        try:
            print(f"{client.user} active")
            synced = await client.tree.sync()
            print(f"synced:\n{synced}")
        except Exception as err:
            print(err)

    @client.tree.command(name="mp3", description="Downloads Mp3 format from YouTube if media is publicly available and not too large")
    @app_commands.describe(url = "url here")
    async def mp3(interaction: discord.Interaction, url: str):
        success: bool = True # is true by default, false if any error occurs        

        # Execute command 
        try:
            name: str = interaction.user.name
            uid: str = interaction.user.id
            media, path = await responses.handle(url)
            await interaction.channel.send(file=media)
            os.remove(path)
            await interaction.response.send_message(f"Here you go, {build_mention(uid)}!")
        except Exception as err:
            print(err)
            success = False
        # Log interaction 
        write_to_history(success, f"{name} {uid}", url, interaction.channel)

    client.run(TOKEN)

    
