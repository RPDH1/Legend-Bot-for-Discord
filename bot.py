import discord

client = discord.Client()

@client.event
async def on_member_join(member):
    # This function is called whenever a new member joins the server
    message = f"Welcome to {member.guild.name}, {member.name}! We're happy you've joined us."
    await member.send(message)

client.run("YOUR_BOT_TOKEN_HERE")
