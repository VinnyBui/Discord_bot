import discord
import os
#from dotenv import load_dotenv
#load_dotenv()

#TOKEN=os.getenv('SECRETKEY')

client = discord.Client()
@client.event
async def on_ready():
  print('Online! {0.user}.'.format(client))

@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}: {user_message} ({channel})')

  if message.author == client.user:
    await message.add_reaction('✅')
    await message.add_reaction('❌')
    return


  if message.channel.name == 'testing':
    if user_message.startswith('!vote'):
      msg = user_message.split('!vote')[1]
      await message.channel.send(f'```Voting on{msg}```')

  if message.content == "!end":
    await client.close()



client.run(TOKEN)
