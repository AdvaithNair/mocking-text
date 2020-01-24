'''
01/24/2020
Advaith Nair
Mockify Discord Bot (Mocking Bird)
Description: I basically stole my mocking function from my last project
and made a fun little Discord bot from it because I was bored
'''

import discord
import random

mock_on = False


def return_mocking(inputText):
    # Input Text Converted to List
    newList = list(inputText.lower())

    # String (Converted to List) Iteration by Character
    for i in range(len(newList)):
        if newList[i] == 'i':
            newList[i] = 'i'  # I want 'i's to be lowercase
        elif newList[i] == 'l':
            newList[i] = 'L'  # I want 'L's to be uppercase
        else:
            # Randomized upper/lower case
            if bool(random.getrandbits(1)):
                newList[i] = newList[i].upper()
            else:
                newList[i] = newList[i].lower()

    # Returns Mocked Text as String
    return "".join(newList)


# Formats Message and Sends
async def send_message(message, msg):
    await message.channel.send(return_mocking(msg.format(message)))


# Bot Class
class MyClient(discord.Client):
    async def on_ready(self):
        print('Username: ' + client.user.name)
        print('UserID: ' + str(client.user.id))

    async def on_message(self, message):
        global mock_on
        # Bot Ignores Its Own Messages
        if message.author.id == self.user.id:
            return

        # Help (Documentation)
        elif message.content == '/help':
            embed = discord.Embed(
                colour=discord.Colour.blue()
            )

            embed.set_author(name='Commands')
            embed.add_field(name='/hello', value='Sends a Friendly Hello Message', inline=False)
            embed.add_field(name='/pacer', value='The FitnessGram Pacer Test...', inline=False)
            embed.add_field(name='/lorem', value='Lorem Ipsum...', inline=False)
            embed.add_field(name='/lol', value='lol', inline=False)
            embed.add_field(name='/kanye', value='Lift Yourself', inline=False)
            embed.add_field(name='/mock [text]', value='returns mOcKeD [text]', inline=False)
            embed.add_field(name='/start', value='Starts Mocking Mode', inline=False)
            embed.add_field(name='/stop', value='Stops Mocking Mode', inline=False)

            await message.channel.send(embed=embed)

        # Simple (Mocked) Hello Command
        elif message.content == '/hello':
            await send_message(message, 'Hello {0.author.mention}, are you ready to get mocked?')

        # Mocks The FitnessGram Pacer Test
        elif message.content == '/pacer':
            msg = 'The FitnessGram Pacer Test is a multistage aerobic capacity test that ' \
                  'progressively gets more difficult as it continues. The 20 meter pacer test ' \
                  'will begin in 30 seconds. Line up at the start. The running speed starts slowly ' \
                  'but gets faster each minute after you hear this signal bodeboop. A sing lap should ' \
                  'be completed every time you hear this sound. ding Remember to run in a straight ' \
                  'line and run as long as possible. The second time you fail to complete a lap before ' \
                  'the sound, your test is over. The test will begin on the word start. On your mark. ' \
                  'Get ready!…'
            await send_message(message, msg)

        # Begins Mock Everything Mode
        elif message.content == '/start':
            if mock_on:
                await message.channel.send('(But I am already mocking you!)'.format(message))
            else:
                mock_on = True
                await message.channel.send('I dare you to start speaking.'.format(message))
            return

        # Stops Mock Everything Mode
        elif message.content == '/stop':
            if mock_on:
                mock_on = False
                await message.channel.send('I win.'.format(message))
            else:
                await message.channel.send('Hey hey, I already stopped mocking you. Relax.'.format(message))
            return

        # Lol
        elif message.content == '/lol':
            embed = discord.Embed(
                colour=discord.Colour.red()
            )

            embed.set_author(name='lol')
            embed.add_field(name='lol', value='lol', inline=False)

            await message.channel.send(embed=embed)

        # Lorem Ipsum
        elif message.content == '/lorem':
            msg = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor ' \
                  'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud ' \
                  'exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure ' \
                  'dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ' \
                  'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt ' \
                  'mollit anim id est laborum.'
            await send_message(message, msg)

        # Kanye (Poopy - discoop)
        elif message.content == '/kanye':
            msg = 'Poopy - discoop\nScoop - diddy - whoop\nWhoop - di - scoop - di - poop\n' \
                  'Poop - di - scoopty\nScoopty - whoop\nWhoopity - scoop, whoop - poop\n' \
                  'Poop - diddy, whoop - scoop\nPoop, poop\nScoop - diddy - whoop\nWhoop - diddy - scoop' \
                  '\nWhoop - diddy - scoop, poop'
            await send_message(message, msg)

        # Mock Everything Mode
        elif mock_on:
            # await message.channel.send(message.content.format(message), tts=True)
            await send_message(message, message.content)

        # Mocks Everything Typed Into Single Line (With Error Handling)
        if message.content == '/mock':
            await send_message(message, 'Come on, give me something to mock!')
        elif message.content.startswith('/mock'):
            await send_message(message, message.content[5:])


# Insert Token Here
TOKEN = 'INSERT TOKEN HERE'

# Running Client
client = MyClient()
client.run(TOKEN)