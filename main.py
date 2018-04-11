import discord, asyncio
client = discord.Client()

#Sneaky, peaky!
#Don't be cheeky!

global Kickmessage
global Banmessage
global Prefix
Kickmessage = open("KickMessage.txt", "r")
Kickmessage = Kickmessage.read()
Banmessage = open("BanMessage.txt", "r")
Banmessage = Banmessage.read()
Prefix = open("Prefix.txt", "r")
Prefix = Prefix.read()

@client.event
async def on_ready():
    print("I'm ready to go!")

@client.event
async def on_message(message):

    global Kickmessage
    global Banmessage
    global Prefix
    
    if message.content.startswith(str(Prefix)+'kick'):
        kicksplit = message.content.split(' ')
        compmessage = ''
        for word in kicksplit[2:]:
            compmessage = compmessage+' '+word
        role = [role.name for role in message.author.roles]
        Kickmessage = Kickmessage.replace("%mod%", str(message.author.mention))
        Kickmessage = Kickmessage.replace("%reason%", str(compmessage))
        if 'kick' in role:
            for member in message.author.server.members:
                if member.id in kicksplit[1]:
                    await client.send_message(member, Kickmessage)
                    await client.kick(member)

    if message.content.startswith(str(Prefix)+'ban'):
        bansplit = message.content.split(' ')
        compmessage = ''
        for word in bansplit[2:]:
            compmessage = compmessage+' '+word
        role = [role.name for role in message.author.roles]
        Banmessage = Banmessage.replace("%mod%", str(message.author.mention))
        Banmessage = Banmessage.replace("%reason%", str(compmessage))
        if 'ban' in role:
            for member in message.author.server.members:
                if member.id in bansplit[1]:
                    await client.send_message(member, Banmessage)
                    await client.ban(member)


        

            
client.run('')
