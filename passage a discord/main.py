import discord
from discord.ext import commands

client = commands.Bot(command_prefix=';')


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
    await ctx.send('Pong')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} a été expulsé pour {reason}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entery in banned_users:
        user = ban_entery.user

        if (user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'c bon {user.name}#{user.discriminator} est déban')
            return



client.run('ODI4NTQ4OTQyNjk3NDYzODI5.YGrMVQ.mFUOhE7b0Owv4LU40pFXsD78198')