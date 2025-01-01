import unittest
from unittest.mock import AsyncMock, MagicMock, patch
import discord
from discord.ext import commands
import main

class TestBotCommands(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.bot = main.client
        self.ctx = MagicMock()
        self.member = MagicMock(spec=discord.Member)
        self.ctx.guild = MagicMock()
        self.ctx.channel = MagicMock()

    async def test_ban(self):
        await main.ban(self.ctx, self.member, reason="test reason")
        self.member.ban.assert_called_with(reason="test reason")
        self.ctx.send.assert_called_with(f'sa dégage {self.member.mention}')

    async def test_clear(self):
        await main.clear(self.ctx, amount=10)
        self.ctx.channel.purge.assert_called_with(limit=10)

    async def test_ping(self):
        await main.ping(self.ctx)
        self.ctx.send.assert_called_with('Pong')

    async def test_kick(self):
        await main.kick(self.ctx, self.member, reason="test reason")
        self.member.kick.assert_called_with(reason="test reason")
        self.ctx.send.assert_called_with(f'{self.member.mention} a été expulsé pour test reason')

    @patch('main.client.change_presence', new_callable=AsyncMock)
    async def test_on_ready(self, mock_change_presence):
        await main.on_ready()
        mock_change_presence.assert_called_with(status=discord.Status.idle, activity=discord.Game('Dokkan Battle'))

    @patch('main.client.guilds', new_callable=MagicMock)
    async def test_unban(self, mock_guilds):
        banned_user = MagicMock()
        banned_user.user.name = "testuser"
        banned_user.user.discriminator = "1234"
        self.ctx.guild.bans = AsyncMock(return_value=[banned_user])
        await main.unban(self.ctx, member="testuser#1234")
        self.ctx.guild.unban.assert_called_with(banned_user.user)
        self.ctx.send.assert_called_with(f'c bon testuser#1234 est déban')

if __name__ == '__main__':
    unittest.main()