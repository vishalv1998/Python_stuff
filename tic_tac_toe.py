#creating user defined exceptions for test cases
class Error(Exception):
	pass
class wrong_spelling_error(Error):
	pass
class space_occupied_error(Error):
	pass
import random
import os#put os.system('clear') somewhere convenient
import numpy as np
#Variables Used for tic Tac Toe
game_state=True
while(game_state):
	os.system('clear')
	globlul=""
	no_of_moves=0
	next_turn=0 # Determines who has the next turn. By default, Player 1 is X and Player 2 is Y
	end_game=True# If this condition goes false, Either somebody won or the game is drawn
	tic_tac_toe=np.asarray([["1","2","3"],["4","5","6"],["7","8","9"]])# Initialize array as 3x3 for tic tac toe
	print("\t\t   Tic Tac Toe\n\n\n")
	def display_board():
		for x in range(3):
			for y in range(3):
				print("\t"+tic_tac_toe[x][y]+"\t",end=" ")
			print("\n")

	display_board()

	def who_goes_first():
		global globlul
		spell_state=True
		while spell_state:
			try:
				print("Let's flip a coin ")
				choice=input("Player 1: What's it going to be? Heads or Tails? ")
				choice_list=["Heads","Tails"]#0,1
				if(choice.lower()!="heads" and choice.lower()!="tails"):
					raise wrong_spelling_error
				spell_state=False
			except wrong_spelling_error:
				print("Wrong Spelling. Try again")

		print("Randomly choosing a choice between Heads and Tails")
		if(choice_list[random.randint(0,1)].lower()==choice.lower()):
			print("Player 1 gets to go first.\nPlayer 1 is X\nPlayer 2 is O")
			player_1="X"
			player_2="Y"
			globlul="1"
		else:
			print("Player 2 gets to go first.\nPlayer 2 is X\nPlayer 1 is O")
			player_1="O"
			player_2="X"
			globlul="2"
		
	def get_inputs():
		space_state=True
		global next_turn
		global no_of_moves
		global globlul
		var=""
		while space_state:
			try:
				print("Player "+globlul+" It's your turn")
				pos=input("Where do you want to enter? select any number from the game board ")
				x=y=count=x1=y1=0
				try:
					for x in range(3):
						for y in range(3):
							if(tic_tac_toe[x][y]==pos):
								count=1
								x1=x
								y1=y
								raise StopIteration()
				except StopIteration:
					pass
				#print(x1) x co-ord
				#print(y1) y co-ord
			#Rewrite this code. Will not work on twice proccing.
				if(count==0):
					raise space_occupied_error
				space_state=False
			except space_occupied_error:
				print("Space is already Occupied. Enter a different position.")
		if next_turn==0:
			tic_tac_toe[x1,y1]="X"
			next_turn=1
			var="X"
		else:
			tic_tac_toe[x1,y1]="O"
			next_turn=0
			var="O"
		no_of_moves+=1	
		verify_win_condition(var,no_of_moves,globlul)	
		if globlul=="1":
			globlul="2"
		else:
			globlul="1"
		display_board()

	def verify_win_condition(var,no_of_moves,globlul):
		x=y=0
		global end_game
		if tic_tac_toe[x][y]==tic_tac_toe[x+1][y+1]==tic_tac_toe[x+2][y+2]==var:
			print("Player "+globlul+" Wins!")
			end_game=False
		if tic_tac_toe[y+2][x]==tic_tac_toe[y+1][x+1]==tic_tac_toe[y][x+2]==var:
			print("Player "+globlul+" Wins!")
			end_game=False
		for x in range(0,3):
			if tic_tac_toe[x][y]==tic_tac_toe[x][y+1]==tic_tac_toe[x][y+2]==var:
				print("Player "+globlul+" Wins!")
				end_game=False
		x=0
		for y in range(0,3):
				if tic_tac_toe[x][y]==tic_tac_toe[x+1][y]==tic_tac_toe[x+2][y]==var:
					print("Player "+globlul+" Wins!")
					end_game=False
		if no_of_moves==9:
			print("It's a draw!")
			end_game=False
	who_goes_first()
	while(end_game):
		get_inputs()	
	end_game_var=int(input("Want to Go Again? 1-Yes 0-No"));
	if end_game_var==0:
		game_state=False