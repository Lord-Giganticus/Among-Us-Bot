const Discord = require('discord.js');

const {prefix, token} = require('./config.json');

const client = new Discord.Client();

client.once('ready', async () => {
    console.log('Ready!')
	client.user.setActivity('A!info')
})

client.on('message', message => {

    if(message.content.startsWith(`${prefix}info`)) {
        message.channel.send("Among Us Bot commands: ```A!info: Displays this. A!invite: Sends the bot invite A!join: Joins the VC you are in. A!dis: Discconects from the VC. A!mute: Mutes all members in the VC. A!unmute: Unmutes all members in the VC.```")
    }

    
})

client.login(token);