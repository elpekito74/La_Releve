const { prefix, token } = require('/config.json');

const { Client, Intents, Collection } = require('discord.js');
const client = new Discord.Client({ intents: ["GUILD_MEMBERS", "GUILD_MEMBER_ADD"]
});
bot.login(token);
