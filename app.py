import discord
from client import client
from src.builder import Builder

@client.event
async def on_ready():
    print('Logged in')
    await client.tree.sync()

@client.command(name='ping', descrpiton='This is a ping command!')
async def ping(interaction: discord.Interaction):
    interaction.response.send_message('Pong')




if __name__ == '__main__':
    client.run()