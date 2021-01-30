import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()			# подключаемся к серверу

# координаты c F3
x = 100
y = 50
z = 100
id_block = 46		# ДИНАМИТ!!!

for y in range(50, 250):
	time.sleep(0.2)
	mc.setBlock(x, y, z, id_block)	# ставит блок

