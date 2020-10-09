const Discord = require('discord.js');

const {prefix, token} = require('./config.json');

const client = new Discord.Client();

client.once('ready', async () => {
    console.log('Ready!')
	client.user.setActivity(`${prefix}info`)
})

client.on('message', message => {

    if(message.content.startsWith(`${prefix}info`)) {
        message.channel.send("Backup Among Us Bot commands: ```A2!info: Displays this. A2!invite: Sends the normal bot invite A2!backup: Sends this bot's invite. A2!join: Joins the VC you are in. A2!dis: Disconects from the VC. A2!mute: Mutes all members in the VC. A2!unmute: Unmutes all members in the VC.```")
    }

    if(message.content.startsWith(`${prefix}invite`)) {
        message.channel.send("https://discord.com/oauth2/authorize?client_id=763810277548228680&scope=bot&permissions=22039552")
    }

    if(message.content.startsWith(`${prefix}backup`)) {
        message.channel.send("https://discord.com/oauth2/authorize?client_id=764110739459670036&scope=bot&permissions=22039552")
    }

    if(message.content.startsWith(`${prefix}join`)) {
        message.member.voice.channel.join();
    }

    if(message.content.startsWith(`${prefix}dis`)) {
       let channel = message.guild.channels.cache.get(message.member.voice.channel.id);
        for (const [memberID, member] of channel.members) {
        member.voice.setMute(false);
        }
       message.member.voice.channel.leave();
    }

    if(message.content.startsWith(`${prefix}mute`)) {
        let channel = message.guild.channels.cache.get(message.member.voice.channel.id);
        for (const [memberID, member] of channel.members) {
        member.voice.setMute(true);
        }
    }

    if(message.content.startsWith(`${prefix}unmute`)) {
        let channel = message.guild.channels.cache.get(message.member.voice.channel.id);
        for (const [memberID, member] of channel.members) {
        member.voice.setMute(false);
        }
    }
})

client.login(token);
