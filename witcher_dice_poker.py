import random as r
print("\t\t\tPOKER DICE")
player_value={
1:"Five of a kind",
2:"Four of a kind",
3:"Fullhouse",
4:"Straight High",
5:"Three of a kind",
6:"Two pairs",
7:"Two of a kind",
8:"Nothing Special"
}

player_1_dice=[]
player_2_dice=[]
numbers=[]
fullhouse=[]
double_pair_count=0
def play_game():
	break_loop=True
	while(break_loop):
		input1=input("Player 1: Press 'r' to roll your dice  ")
		if input1=='r':
			for i in range(5):
				player_1_dice.append(r.randint(1,6))
			break_loop=False
		break_loop=True
		input2=input("Player 2: Press 'r' to roll your dice  ")
		if input2=='r':
			for i in range(5):
				player_2_dice.append(r.randint(1,6))
			break_loop=False
	print("Player 1 has rolled: ")
	print(player_1_dice)
	print("Player 2 has rolled: ")
	print(player_2_dice)
	#player_1_dice = [1,2,4,5,1]
	#player_2_dice = [2,6,3,6,4]
	play_game.player_1_rolls = {i:player_1_dice.count(i) for i in player_1_dice}
	play_game.player_2_rolls = {i:player_2_dice.count(i) for i in player_2_dice}

def get_value(player_rolls):
	global numbers
	global fullhouse
	global double_pair_count
	numbers=[]
	fullhouse=[]
	double_pair_count=0
	for key in player_rolls:
		if player_rolls[key]==5:
			numbers.append(key)
			return 1
		if player_rolls[key]==4:
			numbers.append(key)
			return 2
		if player_rolls[key]==3:
			numbers.append(key)
			fullhouse.append(key)
		if player_rolls[key]==2:
			numbers.append(key)
			double_pair_count+=1
			fullhouse.append(key)
	#test for [3 4 4 4 3]
	#test for [4 5 5 2 6]
	if len(fullhouse)==2 and double_pair_count<2:
		return 3
	elif len(fullhouse)==1 and double_pair_count<1:
		return 5
	if double_pair_count==2:
		return 6
	elif double_pair_count==1:
		return 7
	if player_1_dice==[1,2,3,4,5] or player_1_dice==[2,3,4,5,6]:
		return 4
	return 8
play_game()
def midgame():
	print("Player 1: YOU HAVE ")
	print(player_value[get_value(play_game.player_1_rolls)])
	print("Player 2: YOU HAVE")
	print(player_value[get_value(play_game.player_1_rolls)])
	x=int(input("Player1.Enter the dice position you want to re-roll. press 0 to pass: "))
	if x>0:
		print()
midgame()
player_1_priority=get_value(play_game.player_1_rolls)
player_1_numbers=numbers
player_2_priority=get_value(play_game.player_2_rolls)
player_2_numbers=numbers

def win_condition(player_1_numbers,player_2_numbers,player_1_priority,player_2_priority):
	print("PLAYER 1: YOU HAVE ")
	print(player_value[get_value(play_game.player_1_rolls)])
	print("PLAYER 2: YOU HAVE ")
	print(player_value[get_value(play_game.player_2_rolls)])
	if player_1_priority < player_2_priority:
		print("Player 1 Wins!")
	elif player_1_priority > player_2_priority:
		print("Player 2 Wins!")
	else:
		if max(player_1_numbers) > max(player_2_numbers):
			print("Player 1 Wins!")
		elif max(player_1_numbers) < max(player_2_numbers):
			print("Player 2 Wins!")
		else:	
			if min(player_1_numbers) > min(player_2_numbers):
				print("Player 1 Wins!")
			elif min(player_1_numbers) < min(player_2_numbers):
				print("Player 2 Wins!")
			else:
				print("DRAW!")
win_condition(player_1_numbers,player_2_numbers,player_1_priority,player_2_priority)