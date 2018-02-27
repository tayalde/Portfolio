import discord
import asyncio
import random
from emoji import emojize

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-' * len(client.user.id))

@client.event
async def on_message(message):
    
    # Test messages/connection
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel,
                                        'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    # Sleep example
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    # 100-side die roll
    elif message.content.startswith('!roll'):
        roll = random.randint(0, 100)
        await client.send_message(
            message.channel,
            'You rolled a {}!'.format(roll))

    # Info/help message for bot
    elif message.content.startswith('!info') or message.content.startswith('!help'):
        info = discord.Embed(title='T H I C C',
                             description='T H I C C E S T bot there is...')
        info.set_image(url='http://i0.kym-cdn.com/photos/images/original/001/232/046/190.gif')
        info.add_field(name='!hello',
                       value='Says hello',
                       inline=False)
        info.add_field(name='!test',
                       value='Gives number of your messages from the past 100',
                       inline=False)
        info.add_field(name='!sleep',
                       value='Sleeps the bot for 5 seconds',
                       inline=False)
        info.add_field(name='!roll',
                       value='Rolls a 100-sided die',
               inline=False)
        info.add_field(name='!poker',
                       value='Starts poker app and player selection',
               inline=False)
        await client.send_message(
            message.channel,
            embed=info)

    # Hello command
    elif message.content.startswith('!hello'):
        # TODO: New member/logon activation
        hello = discord.Embed(title='こんにちは')
        hello.set_image(url='http://www.reactiongifs.com/r/hello-bear.gif')

        await client.send_message(
            message.channel,
            embed=hello)

    # Starts Texas Hold'em 
    elif message.content.startswith('!poker'):
        # TODO: Integrate poker app
        poker = discord.Embed(title="Texas Hold'em!",
                              description='Select your position!')
        poker.add_field(name='Player One', value=':koala:', inline=False)
        poker.add_field(name='Player Two', value=':man_with_turban:', inline=False)
        poker.add_field(name='Player Three', value=':eggplant:', inline=False)
        poker.add_field(name='Player Four', value=':beetle:', inline=False)
        msg = await client.send_message(
            message.channel,
            embed=poker
            )

        reactions = [u'\U0001F428', u'\U0001F473', u'\U0001F346', u'\U0001F41E']
        users = []

        while reactions:
            res = await client.wait_for_reaction(reactions, message=msg)
            await client.send_message(message.channel, '{0.user} reacted with {0.reaction.emoji}!'.format(res))
            print(res)
            reactions.remove(res[0].emoji)
            users.append(res[1])
            for user in users:
                print(user.id)

client.run('NDE2MzgzOTIxNzA2NjMxMTc5.DXDtRg.275Eb9tq_5YSg1TFURAAiy6BISo')
