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

    if(message.content.startsWith(`${prefix}invite`)) {
        message.channel.send("https://discord.com/oauth2/authorize?client_id=763810277548228680&scope=bot&permissions=22039552")
    }

    if(message.content.startsWith(`${prefix}join`)) {
        message.member.voice.channel.join();
    }

    if(message.content.startsWith(`${prefix}dis`)) {
        message.member.voiceChannel.leave();
    }

    if(message.content.startsWith(`${prefix}mute`)) {
        let channel = message.member.voiceChannel;
        for (let member of channel.members) {
            member[1].setMute(true)
        }
    }

    if(message.content.startsWith(`${prefix}unmute`)) {
        let channel = message.member.voiceChannel;
        for (let member of channel.members) {
            member[1].setMute(flase)
        }
    }
})

client.login(token);