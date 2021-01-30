list_game = ["CS GO", "Minecraft", "Mafia", "GTA 5", "Far Cry 3"]




print(10)






















# "не очень" хороший способ перечислить список
print(list_game[0])
print(list_game[1])
print(list_game[2])

print(list_game)

print()

# цикл for in для перечисления списка - лучший способ
for game in list_game:
	print(game)

print()


# цикл while для перечисления списки
i = 0
game = len(list_game)
while i < game:
	print(list_game[i])
	i = i + 1

  
