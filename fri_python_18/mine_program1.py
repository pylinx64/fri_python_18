from mcpi.minecraft import Minecraft
mc = Minecraft.create()			# подключаемся к серверу

# координаты
x = 100
y = 200
z = 100

mc.player.setPos(x, y, z)


