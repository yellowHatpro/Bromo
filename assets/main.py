import discord
from discord.ext import commands , tasks
import aiohttp
import random
import os
from dotenv import load_dotenv
import random
import random2
import requests


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# discord.intents.all role is to allow the bot to see all the roles in the server
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='>' , intents = intents)



#variables
statuses = ['vscode','sublime text', 'python', 'discord.py', 'bromo', 'bromo.py', 'bromo.py']
#events:


    

@tasks.loop(seconds=10000)
async def change_status():
    await client.change_presence(activity=discord.Game(random.choice(statuses)))

    
@client.event
async def on_ready():
    
    print('Bot is ready')  
    change_status.start() #starts the loop
@client.event
async def help(ctx):
    await ctx.send('help')



#commands    

@client.command()
async def meme(ctx=None):
    pymeme = discord.Embed(title="Test", description="Test", color=0xe91e63)
    # now getting memes from api using requests
    # https://meme-api.herokuapp.com/gimme
    # https://meme-api.herokuapp.com/gimme/dank
    # https://meme-api.herokuapp.com/gimme/spongebob
    requests.get('https://meme-api.herokuapp.com/gimme/dank')
    # now getting the json data
    data = requests.get('https://meme-api.herokuapp.com/gimme/dank').json()
    # now getting the image url
    image = data['url']
    # now getting the title
    title = data['title']
    # now getting the subreddit
    subreddit = data['subreddit']
    # now using the embed to add the image and title
    pymeme.set_image(url=image)
    pymeme.set_footer(text=f'Subreddit: {subreddit}')
    pymeme.set_author(name=title)
    # now sending the embed
    await ctx.send(embed=pymeme)

    
@client.command(aliases=['user','info'])
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title = member.name , description = member.id , color = discord.Color.blue()) 
    embed.add_field(name = "ID", value = member.id, inline = True)   
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text = "User Info")
    await ctx.send(embed = embed)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 "Don't count on it.",
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.',
                 'No.',
                 'No chance.',
                 'No way.',
                 'Not a chance.',
                 'Not a possibility.',
                 'Not a good idea.',
                 'Not in a million years.',
                 'Not likely.',
                 "Don't know, didn't ask,plus you are sus. ",
                    'Not sure.',
                 ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#playing a game in the server
@client.command()
async def game(ctx, *, game):
    await client.change_presence(activity=discord.Game(name=game))
    await ctx.send(f'Now playing {game}')
    



client.run(TOKEN)
