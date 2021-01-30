import pyttsx3
import random
import webbrowser


# Настройки голоса
tts = pyttsx3.init()	# голосовой движок
tts.setProperty('voice', 'ru')  # Наш голос по умолчанию
tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)
tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)


# Все команды для ассистента
def say_assistant(msg):
	tts.say(msg) # добавляет реплику
	print(msg)
	tts.runAndWait() # Воспроизвести очередь реплик
	
# TODO: команда для поиска на ютьюб видео
	
	
# Фразы для бота
MESSAGE_HELLO = ['Хай', 'Привет', 'Нихао', 'Адьйос', 'Ку']
MESSAGE_ERRORS = ['Я вас не понимаю', 'Еррор', 
				  'Хьюстон у нас проблемы', 'ПХПХХХПХ']
	
	
# Запоминает имя
say_assistant('Привет, я ъъъ А как тебя зовут?')
NAME = input('->')
say_assistant('Привет, ' + NAME)


# Основной цикл ассистента (основной код программы)
while True:
	say_assistant('Введи команду, ' + NAME)
	command = input()
	if 'как дела' in command:
		say_assistant('окей, ' + NAME)
	elif 'норм?' in command:
		say_assistant('норм, ' + NAME)
	elif 'привет' in command:
		say_assistant(random.choice(MESSAGE_HELLO) + ' ' + NAME)
	else:
		say_assistant(random.choice(MESSAGE_ERRORS) + ' ' + NAME)
