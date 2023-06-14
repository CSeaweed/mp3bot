import discord
import responses
import json


async def send_message(msg, user_msg, private):
    try:
        response: str = responses.handle(user_msg)
        await msg.channel.send(response)        
    except Exception as err:
        print(err)

def get_secrets(secret: str) -> dict:
    secrets: dict = {}
    with open(secret, encoding="utf-8", mode="r") as data:
        secrets = json.load(data)
    return secrets

def run_bot():
    secret_file = "./secrets.json"
    SECRETS: dict = get_secrets(secret_file)    
    TOKEN, INV = SECRETS["TOKEN"], SECRETS["INV"]



if __name__ == "__main__":
    run_bot()

    

