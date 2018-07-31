# bulls and cows is an old code breaking game. Create a porgram that will play a game with the user. The working of the game is as follows:
# 1. Randomly generate a 4 digit number
# 2. Ask the user to guess the 4 digit number
# 3. For every digit that the user guessed correctly in the correct place, they have a cow
# 4. For every digit that the user guessed correctly in the wrong place, they have a bull
# 5. Every time the user makes a guess, tell him how many cows and bulls he has
# 6. Once the user guesses the correct number, the game is over
# 7. Keep track of the number of guesses that the user makes throughout the game and tell the user at the end.

# Ex: say the number generated randomly is 1038. For the first guess, the user enters 1234. He has 2 cows and 0 bulls
# Now, the second guess is 1256. He now has 1 cow and 0 bulls.
import random
number_to_guess=random.randint(1000, 9999)
number_to_guess_list=[x for x in str(number_to_guess)]
print(number_to_guess_list)
number_of_guesses=0
while(1):
	cow=0
	bull=0
	input_guess=input("Enter a 4 digit number: ")
	if(len(input_guess)==4):
		for i in range(len(input_guess)):
			if input_guess[i]==number_to_guess_list[i]:
				cow+=1
			elif input_guess[i] in number_to_guess_list:
				bull+=1
		number_of_guesses+=1
		print("COW ",cow)
		print("BULL",bull)
		print("Guesses ",number_of_guesses)
		if(cow==4):
			print("Correct Guess")
			exit(0)
	else:
		print("Enter valid number")