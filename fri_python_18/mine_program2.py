from mcpi.minecraft import Minecraft
mc = Minecraft.create()			# подключаемся к серверу

# координаты c F3
x = 100
y = 200
z = 100
id_block = 56

mc.setBlock(x, y, z, id_block)
