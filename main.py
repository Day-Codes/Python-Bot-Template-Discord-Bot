import discord
import os
from discord.ext import commands
import keep_alive
import random 

# Made By Dayln - DO NOT REMOVE CREDITS! Join our support server in the github rospository!


client = commands.Bot(command_prefix = commands.when_mentioned_or("PREFIX HERE!"),case_insensitive=True, help_command=None)
# To make your own help command: help_command=None (Remove if you dont want to make one)
@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
        print('Hello!')
        print('Made by: Days Code')
        print('Bot Loaded!')
        print(f'I have successfully logged in as {client.user.name}#{client.user.discriminator}!')
        print(f'Template is made by: days-codes.')

@client.command()
async def help(ctx): 
        embed = discord.Embed(title="Help command!", description="", color=0x00FFFF)
        embed.add_field(name=f"[$/@]help", value="Shows this message!", inline=False)
        

        await ctx.message.delete()
        await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator = True)
async def setdelay(ctx, seconds: int):
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked.')

@client.command(description='Bans a Member: Admin Perms Only')
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
	if reason == None:
		await user.ban(reason=reason)
		await ctx.send(f'{user} was banned by {ctx.author.mention} | Reason: **NO REASON PROVIDED**')
	else:
		await user.ban(reason=reason)
		await ctx.send(
		    f'{user} was banned by {ctx.author.mention} | Reason: **{reason}**')


@client.command()
async def test(ctx):
    await ctx.send('Test us done! That bot is working.')


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def commandtemplate(ctx):
  await ctx.send('command base')
  await ctx.message.delete()

@client.command()
async def say(ctx, *, arg):
	embed = discord.Embed(title="", description=f"{arg}\n", color=0x00FFFF)
	await ctx.message.delete()
	await ctx.send(embed=embed)

@client.command()
async def members(ctx):
        embed = discord.Embed(title="", description="", color=0x00FFFF)
        embed.add_field(name="Member Count:", value=f"There are currently **{ctx.guild.member_count}** in **{ctx.guild.name}**!", inline=False)
        await ctx.send(embed=embed)
        await ctx.message.delete()

@client.command(pass_context = True)
async def kill(ctx, member: discord.Member):
    kill_messages = [
        f'{ctx.message.author.mention} killed {member.mention} with a baseball bat!', 
        f'{ctx.message.author.mention} killed {member.mention} with a frying pan!',
        f'{ctx.message.author.mention} tried to kill {member.mention} by burning his hands off, but {member.mention} pulled a tricky-trick and burnt {ctx.author.mention}\'s hands off instead ;)',
        f'{ctx.message.author.mention} attempted to murder {member.mention} but .. NAH!'
    ]  # This is where you will have your kill messages. Make sure to add the mentioning of the author (ctx.message.author.mention) and the member mentioning (member.mention) to it
    await ctx.send(random.choice(kill_messages))
    await ctx.message.delete()

@client.command(pass_context = True)
async def coinflip(ctx):
    coin = [
        f'Head', 
        f'Tails',f'IDFC']
        
   
    await ctx.send(random.choice(coin))
    await ctx.message.delete()



@client.command()
async def cool(ctx, member: discord.Member):
  await ctx.send(f'{member.mention} {ctx.author.mention} thinks your cool')
  await ctx.message.delete()




token = os.environ.get("TOKEN")
client.run(token)