import pyttsx3

tts = pyttsx3.init()	# голосовой движок
tts.setProperty('voice', 'ru')  # Наш голос по умолчанию
tts.setProperty('rate', 150)    # Скорость в % (может быть > 100)
tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)

def say_assistant(msg):
	tts.say(msg) # добовляет реплику
	print(msg)
	tts.runAndWait() # Воспроизвести очередь реплик

say_assistant('Введи свое имя')
NAME = input('-> ')
say_assistant('Окей, а меня зовут Дори!')
while True:
	say_assistant(NAME+ ' введи команду пж:')
	command = input('->')
	if 'привет' in command:
		say_assistant(NAME + ' ну хай')
	elif 'дела' in command:
		say_assistant(NAME + ' норм')
	elif 'браузер' in command:
		webbrowser.open('https://www.youtube.com/?hl=uk&gl=UA')
		say_assistant(NAME + ' браузер открыт')
