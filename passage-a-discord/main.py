import os
import certifi
import discord
from discord.ext import commands

os.environ['SSL_CERT_FILE'] = certifi.where()

intents = discord.Intents.default()
intents.members = True  # Enable the members intent

client = commands.Bot(command_prefix=';', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,
                                 activity=discord.Game('Dokkan Battle'))
    print("Je suis la mon pote, tout fonctionne parfaitement !")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'sa dégage {member.mention}')


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'c bon {user.name}#{user.discriminator} est déban')
            return


client.run('ODI4NTQ4OTQyNjk3NDYzODI5.GjEGY8.VOx-vxUFfaAYPuLBvBL1A_lGQELCfV8k4D7kWM')

