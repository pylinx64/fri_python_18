import random

money = 10000

while True:
	print("-----------------------------------")
	print("Баланс: ", money)
	print("$$$	Привет, ты хочешь кэш???	$$$")

	rand_number = random.randint(1, 10)

	player_number = input("Введите выигрышное число (от 1 до 10) -> ")

	if str(rand_number) == player_number:
		print("$$$$$$$$$	You win		$$$$$$$$$$")
		money = money + random.randint(1000, 2000)

	elif (player_number == 'q') or (money <= 0):
		print("@			Stop Game			 @")
		break
	else:
		print("				Game over			  ")
		money = money - random.randint(1000, 2000)
	print(money)
 
