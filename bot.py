import discord
from handler import handle_response

intents = discord.Intents.default()

async def send_mesagge(message, user_message, is_private):
    try:
        response = handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(f"This exception: {e}")

def run_discord_bot():
    TOKEN = "MTA5Mjk5MDI4Mzk2MjEzODczNA.GJclxP.xByLz6WroXH3mglI_kGzYsvojlBSQDlIQjssC8"
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):

        if message.author == client.user:
            return

        username = str(message.author)  #.split('#')[0]
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username}: {user_message} ({channel})')

        if str(user_message[0]) == "$":
            user_message = user_message[1:]
            await send_mesagge(message, user_message, is_private=True)
        else:
            await send_mesagge(message, user_message, is_private=False)
    client.run(TOKEN)

