import discord
from discord.ext import commands


def readtoken():
    with open("token", "r") as f:
        lines=f.readlines()
        return lines[0].strip()


token = readtoken()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.command(name='list_roles')
async def list_roles(ctx):
    guild = ctx.guild
    everyone = "@everyone"
    response = f"{[role.name for role in guild.roles if role.name!= everyone]}"
    await ctx.send(response)


@bot.command(name='list_members')
async def list_members(ctx):
    guild = ctx.guild
    response = f"{[member.name for member in guild.members]}"
    await ctx.send(response)


@bot.command(name='create_channel')
@commands.has_role('12-13-14')
async def create_channel(ctx, channel_name='123'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)


bot.run(token)
