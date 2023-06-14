import discord
import responses


async def send_message(msg, user_msg, private):
    try:
        response: str = responses.handle(user_msg)
        await msg.channel.send(response)        
    except Exception as err:
        print(err)

def run_bot():


