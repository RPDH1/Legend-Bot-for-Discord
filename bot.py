import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_member_join(member):
    message = f"Welcome to {member.guild.name}, {member.name}! We're happy you've joined us."
    await member.send(message)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ping"):
        await message.channel.send("pong")

client.run("YOUR_BOT_TOKEN_HERE")
