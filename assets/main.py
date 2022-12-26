import discord
from discord import app_commands
import os
from dotenv import load_dotenv
import random
import requests


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")


load_dotenv()
TOKEN = os.getenv('TOKEN')

client = aclient()
tree = app_commands.CommandTree(client)


@client.event
async def help(ctx):
    await ctx.send('help')

# commands


@tree.command(name="userinfo", description="Tells user info")
async def userinfo(interaction: discord.Interaction, member: discord.Member):
    roles = [str(role.name) for role in member.roles]
    if ("@everyone" in roles):
        roles.remove("@everyone")
    embed = discord.Embed(
        title=member.name,
        description=' '.join([role for role in roles]),
        color=discord.Color.blue())
    embed.add_field(name="ID",
                    value=member.id,
                    inline=True)
    embed.set_author(
        name="Bromo", icon_url="https://drive.google.com/file/d/1C1xc0VGIbyofDpCmpHlHdJ3xRbDi6iB4/view?usp=share_link")
    embed.set_image(url=member.display_avatar)
    await interaction.response.send_message(embed=embed)

client.run(TOKEN)
