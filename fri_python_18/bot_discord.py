import discord
import datetime


# сообщения-тригеры для человека
message_hello = ['привет', 'ку', 'хай', 'hello', 'дароу']
TOKEN = 'ODM1MTgxMTU1NjU3MTg3NDA4.YILtEA.2PZXgKGYWpN_MQ1jNKlauzSrQnQ'
client = discord.Client()


@client.event
async def on_message(message):
    # проверка на других ботов
    if message.author.bot == True:
        return
    
    # message.author - хранится автор
    # message.content - хранится текст сообщения
    # message.guild - хранится сервер 

    print(f'--- автор: {message.author} | сообщение: {message.content} | сервер: {message.guild} | канал: {message.channel} | время: {str(datetime.datetime.now())}---')
    
    # префикс (бот отвечает только на сообщения если в начале есть "!")
    #if '!' != message.content.lower()[0]:
    #    return
    
    if set(message_hello) & set(message.content.lower().split()):
        # отправляет сооб
        await message.channel.send('Ни хао 🦿')
    


client.run(TOKEN)
