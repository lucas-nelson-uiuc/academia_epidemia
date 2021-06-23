### IMPORT LIBRARIES
import profile
import random

### CREATE PLAYER
class Player:

	def __init__(self):
		self.name = input('What is your name?\n> ').title()
		self.games_won  = 0
		self.games_lost = 0

# variables for pretty printing
filler1 = "------------------------"
filler2 = "========================"

def blackjack2(name, games_won, games_lost, iterations):
	### Welcome to blackjack2! This python script will allow you to create a user instance of your own blackjack game
	### and keep track of games won and (more likely) games lost.

	### USER SECTION ###
	if (games_won == 0) & (games_lost == 0):
		print(filler2 * 2); print(f"Welcome to blackjack2, {name}!"); print(filler1 * 2)
		print("RULES:"); print(filler1 * 2)
		print("""
			Objective: Beat the dealer by getting as close to 21 as possible without going over 21
			However, in blackjack2, the dealer always achieves 20.5, so the only winning hand is 21.

			Scoring  : Numerical cards assume pip value. Face cards assume 10. Aces are 1 unless 11
			does not conclude the game (i.e. score over 21).

			Playing  : Cards are dealt one-by-one until the game ends, either by achieving 21 or
			going over 21.
			""")

		buffer1 = input("Do you understand the rules?\n> ")
		buffer2 = input("Good for you. Press ENTER to play!\n> [INSERT TOKEN]")
	else:
		buffer2 = input("Good for you. Press ENTER to play!\n> [INSERT TOKEN]")
	
	### GAME ARCHITECTURE ###
	deck = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':[1, 11]}
	game_count = 0

	while (game_count < iterations):
		print(filler2 * 2); print("GAME COUNT: {}".format(game_count + 1)); print(filler1 * 2)
		hand_sum = 0
		
		while (hand_sum < 21):
			dealt_card = random.choice(list(deck.keys()))

			# account for special case: aces
			if (dealt_card == "ace"):
				if hand_sum + 11 > 21:
					print("Dealt card : " + str(dealt_card))
					hand_sum += deck[dealt_card][0]
					print("Current sum: " + str(hand_sum))
				else:
					print("Dealt card : " + str(dealt_card))
					hand_sum += deck[dealt_card][1]
					print("Current sum: " + str(hand_sum))

			# account for all other non-ace cases
			if (dealt_card != 'ace'):
				print("Dealt card : " + str(dealt_card))
				hand_sum += deck[dealt_card]
				print("Current sum: " + str(hand_sum))
			
			# if hand_sum remains less than 21
			if (hand_sum < 21):
				continue
			
		print(filler2 * 2)
		# game condition two: success
		if (hand_sum == 21):
			games_won += 1
			print(f"GAME OVER: You have won {games_won} and lost {games_lost} games of blackjack."); print(filler1 * 2)
		
		# game condition three: loss
		if (hand_sum > 21):
			games_lost += 1
			print(f"GAME OVER: You have won {games_won} and lost {games_lost} games of blackjack."); print(filler1 * 2)

		# DO NOT FORGET TO UPDATE game_count
		game_count += 1
			
	# prompt decision to start new game
	result = [name, games_won, games_lost]
	endgame_decision(result)


# prompt player to play new game; reached if hand_sum >= 21
def endgame_decision(result):
	prompt = input('Would you like to start a new game? yes or no\n> ')
	if prompt.lower() == 'yes':
		iterations = int(input('How many games would you like to play? Enter a number\n> '))
		blackjack2(result[0], result[1], result[2], iterations)
	if prompt.lower() == 'no':
		print(filler2 * 2); print(f"{result[0]}, you won {result[1]} games and lost {result[2]} games. Better luck next time!"); print(filler2 * 2)


### CALLING IN TERMINAL
if __name__ == '__main__':
	player = Player()
	iterations = int(input('How many games would you like to play? Enter a number\n> '))
	profile.run('print(blackjack2(player.name, player.games_won, player.games_lost, iterations)); print()')