import discord
import os
import random
from discord import app_commands, Color
from dotenv import load_dotenv
from urllib.error import HTTPError
from api import leetcode_api


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


@tree.command(name="leetcode_random", description="Gives random leetcode question")
async def leetcode_random(interaction: discord.Interaction):
    questions = leetcode_api.random_leetcode_problem()
    if len(questions) != 0:
        question_stat = [q["stat"] for q in questions]
        question = random.choice(question_stat)
        q = question["question__title_slug"]
        embed = discord.Embed(
            title=question["question__title"],
            description=f"[https://leetcode.com/problems/{q}](https://leetcode.com/problems/{q})",
            color=Color.blue()
        )
        await interaction.response.send_message(embed=embed)
    else:
        return


@tree.command(name="leetcode_daily", description="Today's leetcode question")
async def leetcode_daily(interaction: discord.Interaction):
    try:
        q = leetcode_api.get_daily_problem_as_dict()
        data = q["data"]["activeDailyCodingChallengeQuestion"]
        question = data["question"]
        question_name = question["title"]
        question_id = question["frontendQuestionId"]
        question_difficulty = question["difficulty"]
        topic_tags = question["topicTags"]
        question_slug = question["titleSlug"]
        link = f"https://leetcode.com/problems/{question_slug}"

        embed = discord.Embed(
            title=f"{question_id}. {question_name}",
            description=f"Difficulty: {question_difficulty} \n ",
            url=link
        )
        await interaction.response.send_message(embed=embed)
    except HTTPError:
        return


@tree.command(name="userinfo", description="Tells user info")
async def userinfo(interaction: discord.Interaction, member: discord.Member):
    roles = [str(role.name) for role in member.roles]
    if "@everyone" in roles:
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
