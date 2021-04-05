import discord
import os
from dotenv import load_dotenv

commands = {'boba', 'order'}
teas = {'milk', 'fruit'}
milk_types = {'classic', 'thai', 'strawberry', 'wintermelon', 'taro', 'brown_sugar'}
fruit_types = {'grapefruit', 'mango', 'passionfruit', 'lychee', 'peach', 'honeydew'}
toppings = {'boba', 'jelly', 'pudding'}
#referenced my own boba presentation: https://docs.google.com/presentation/d/1_ijyh5v3hp1fIQyGt6sa_AHi4nIx2dDAbIfhfjelUnk/edit?usp=sharing

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await self.change_presence(activity=discord.Game(name="start your message with ! to summon me! :)"))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        #commands
        commands = []
        if message.content[0] == '!': #prefix
            commands = message.content[1:].split(" ")

            if commands[0] == 'boba':
                await message.channel.send('that\'s the magic word!')
            #boba order
            elif commands[0] == 'order':
                if len(commands) < 4:
                    await message.channel.send('please use this format to order: \n!order [tea] [type] [topping]')
                    return
                if commands[1] not in teas:
                    await message.channel.send('sorry, we only have milk or fruit tea right now!')
                elif commands[1] == 'milk' and commands[2] not in milk_types:
                    await message.channel.send('sorry, we only have the following milk types: ' + ', '.join(milk_types))
                elif commands[1] == 'fruit' and commands[2] not in fruit_types:
                    await message.channel.send('sorry, we only have the following fruit types: ' + ', '.join(fruit_types))
                elif commands[3] not in toppings:
                    await message.channel.send('sorry, we only have boba, jelly, or pudding toppings right now!')
                else:
                    await message.channel.send('congrats! you ordered a {} {} tea with {}'.format(commands[2],commands[1],commands[3]))
            else:
                await message.channel.send('hiya! currently the only commands are !boba and !order :)')


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = MyClient()
client.run(TOKEN) #token