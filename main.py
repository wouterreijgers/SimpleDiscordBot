import asyncio
import random

import discord


#Token that connects with the bot
TOKEN = 'NzgxOTU2NTYyMTAwNDIwNjA4.X8FLzA.S_4caD0aKvK62K51MqG2Tely-dM'

client = discord.Client()

alive = True
channels = []

reply = ['Mijn gemeente heeft rond de 41.000 inwoners',
         'Je kan campussen van de UA vinden in de gemeente waar ik woon',
         'Ik woon niet ver van een Fort',
         'Als ge zat zijt, kunt ge op minder dan een half uur van de vizit tot bij mij thuis wandelen']


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(message)
    command = message.content.split(' ')
    if command[0] == 'bot':
        channel = client.get_channel(int(command[1]))
        if command[2] == 'conv_biokot':
            await asyncio.sleep(12)
            await channel.send(
                'Awel das goe, dan babbel ik rechts van u wel met toffere mensen.')
        if command[2] == 'conv_hagar':
            await asyncio.sleep(16)
            await channel.send(
                'Ik hoor het al Thomas, gij vindt mij genen toffe. Ik zal me wel aan de rechterkant van de tafel '
                'zetten, zet gij u maar bij die middelste drie aan tafel. ‘T is al goe.')
        if command[2] == 'conv_all':
            await asyncio.sleep(2)
            await channel.send(
                'Awel das goe, dan babbel ik rechts van u wel met toffere mensen.')
            await channel.send(
                'Ik hoor het al Thomas, gij vindt mij genen toffe. Ik zal me wel aan de rechterkant van de tafel '
                'zetten, zet gij u maar bij die middelste drie aan tafel. ‘T is al goe.')
    print(message.channel.type)
    if not message.guild:
        if 'waar' in message.content or 'Waar' in message.content:
            await message.channel.send(reply[random.randint(0, len(reply)-1)])





@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


if __name__ == '__main__':
    client.run(TOKEN)
