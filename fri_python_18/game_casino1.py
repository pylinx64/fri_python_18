import random
import time

money = int(input("> Введите кеш: "))
t = 0.5

while True:
	print("-----------------------------------")
	time.sleep(t)
	print("Баланс: ", money)
	time.sleep(t)
	print("$$$	Привет, ты хочешь кэш???	$$$")
	time.sleep(t)

	rand_number = random.randint(1, 10)

	player_number = random.randint(1, 10)

	if rand_number == player_number:
		print("$$$$$$$$$	You win		$$$$$$$$$$")
		time.sleep(t)
		money = money + random.randint(1000, 2000)

	elif (player_number == 'q') or (money <= 0):
		print("@			Stop Game			 @")
		time.sleep(t)
		break
	else:
		print("				Game over			  ")
		time.sleep(t)
		money = money - random.randint(1000, 2000)
		print(rand_number)
		print(player_number)
	print(money)
	time.sleep(t)
	time.sleep(0.5)
 
