import discord
import random

TOKEN = 'ODgyMTA5Njc2MTE5MDExMzM4.YS2mpw.DVn5838VjRjZ8qfdcWmZU0_bFzU'

client = discord.Client()

@client.event
async def on_ready():
  print('Sup bitches {0.user}.'.format(client))

client.run(TOKEN)