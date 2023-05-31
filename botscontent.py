import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    async def on_message(self, message):
        if message.content.startswith('!deleteme'):
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()

            await message.channel.send('Goodbye in 3 seconds...', delete_after=3.0)

    async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)
        self.role_message_id = 0
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 0,
            discord.PartialEmoji(name='🟡'): 0,
            discord.PartialEmoji(name='green', id=0): 0,
        }

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        """Gives a role based on a reaction emoji."""

        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:

            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:

            return

        role = guild.get_role(role_id)
        if role is None:

            return

        try:

            await payload.member.add_roles(role)
        except discord.HTTPException:

            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        """Removes a role based on a reaction emoji."""
        if payload.message_id != self.role_message_id:
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:

            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:

            return

        role = guild.get_role(role_id)
        if role is None:

            return


        member = guild.get_member(payload.user_id)
        if member is None:

            return

        try:

            await member.remove_roles(role)
        except discord.HTTPException:

            pass

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
bot.run("token")
