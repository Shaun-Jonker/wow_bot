import discord
import random
import time
import logging
from discord.ext import commands
import csv
from writer import Writer


class Economy(commands.Cog):
    ...

    async def withdraw_money(self, member, money):
        # implementation here
        ...

    async def deposit_money(self, member, money):
        # implementation here
        ...


class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def coinflip(self):
        return random.randint(0, 1)

    @commands.command()
    async def gamble(self, ctx, money: int):
        """Gambles some money."""
        economy = self.bot.get_cog('Economy')
        if economy is not None:
            await economy.withdraw_money(ctx.author, money)
            if self.coinflip() == 1:
                await economy.deposit_money(ctx.author, money * 1.5)