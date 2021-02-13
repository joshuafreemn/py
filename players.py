players = ['charles', 'martina', 'micheal', 'florance', 'ell']
	
	#player 0 to 2
print("Players 0 to 2:")
print(players[0:3])
print("\n")
	#player 1 to 3
print("Players 2 to 4:")
print(players[1:4])
print("\n")
	#player 0 to 4
print("Players upto 3:")
print(players[:4])
print("\n")
	#players 2 to -1
print("Players 3 til infinty:")
print(players[2:])
print("\n")
	#the last 2 players
print("Last 2 players:")
print(players[-2:])
print("\n")
	#every other player
print("Everyother player:")
print(players[0:5:2])
print("\n")
	
	#loopin tha slice
print("Here are the first player o my team:")
for player in players[:3]:
	print(player.title())