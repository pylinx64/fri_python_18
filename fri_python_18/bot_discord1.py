import discord


TOKEN = 'ODM1MTgxMTU1NjU3MTg3NDA4.YILtEA.Jko6c3hT0bfscs0HnuUJvjiqzos'
client = discord.Client()


@client.event
async def on_message(message):
    # проверка что бот не четает свои же сообщения
    if message.author == client.user:
        return
        
    # проверка на других ботов
    if message.author.bot == True:
        return
    
    print(message.author, message.content)
    
    # отправляет сооб
    await message.channel.send(message.content)
    


client.run(TOKEN)
