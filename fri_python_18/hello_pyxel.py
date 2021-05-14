import pyxel
import random

class App:
	def __init__(self):
		# создание окошка
		pyxel.init(256, 256, caption='My game 2010')
		
		# добавляет мышку 
		pyxel.mouse(True)
		
		# запуск программы 
		pyxel.run(self.update, self.draw)
		
	def update(self):
		pass
		
	def draw(self):
		pyxel.text(128, 128, 'TTTTTTT', random.randint(0, 15))

	
App()
		
