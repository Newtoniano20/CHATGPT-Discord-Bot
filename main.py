import discord
import openai
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "chatgpt", description = "Ask Something to chatgpt")
async def first_command(interaction: discord.Interaction, request: str):
    await interaction.response.defer()
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(request),
            temperature=0.6,
            max_tokens=50
    )
    print(response)
    await interaction.followup.send(str(response.choices[0].text))
    #await interaction.response.send_message(request)
    
def generate_prompt(request):
    return f"{request}"

@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(os.getenv("DISCORD_KEY"))