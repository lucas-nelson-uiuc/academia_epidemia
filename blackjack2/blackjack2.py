# Simulation of blackjack with terminal and graphing functionality.
# Contains multiple points of user input and file writing, but is
# kept within a controlled environment for no user interference.

import profile
import random
import bj_analysis

class Player:

	def __init__(self):
		self.name = input('What is your name?\n> ').title()
		self.games_won  = 0
		self.games_lost = 0

filler1 = "------------------------"
filler2 = "========================"

def simulation(name, games_won, games_lost, iterations=1, cycles=0):
	"""Simulates blackjack game a specified number of iterations.

    If cycles positive, multiple blackjack simulations of specificed
    iteration length will be played and tracked per cycle (all of
    equal length).

    Results stored in separate .csv files for analysis and
    graph plotting (terminal only).
	"""

	if (games_won == 0) & (games_lost == 0):
		print(filler2 * 2); print(f"Welcome to blackjack2, {name.title()}!"); print(filler1 * 2)
		print("RULES:"); print(filler1 * 2)
		print("""
			Objective: Beat the dealer by getting as close to 21 as possible without going over 21
			However, in blackjack2, the dealer always achieves 20.5, so the only winning hand is 21.

			Scoring  : Numerical cards assume pip value. Face cards assume 10. Aces are 1 unless 11
			does not conclude the game (i.e. score over 21).

			Playing  : Cards are dealt one-by-one until the game ends, either by achieving 21 or
			going over 21.
			""")

		buffer2 = input("Press ENTER to play!\n> [INSERT TOKEN]")
	
	cycle = 0
	game_count = 0
	deck = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':[1, 11]}

	
	while (game_count < iterations):
		print(filler2 * 2); print("GAME COUNT: {}".format(game_count + 1)); print(filler1 * 2)
		hand_sum = 0
		
		while (hand_sum < 21):
			
			dealt_card = random.choice(list(deck.keys()))

			if (dealt_card == "ace"):
				if hand_sum + 11 > 21:
					print("Dealt card : " + str(dealt_card))
					hand_sum += deck[dealt_card][0]
					print("Current sum: " + str(hand_sum))
				else:
					print("Dealt card : " + str(dealt_card))
					hand_sum += deck[dealt_card][1]
					print("Current sum: " + str(hand_sum))

			if (dealt_card != 'ace'):
				print("Dealt card : " + str(dealt_card))
				hand_sum += deck[dealt_card]
				print("Current sum: " + str(hand_sum))
			
			# game condition one: undetermined
			if (hand_sum < 21):
				continue
			
		print(filler2 * 2)
		# game condition two: success
		if (hand_sum == 21):
			games_won += 1
			print(f"GAME OVER: You have won {games_won} and lost {games_lost} games of blackjack2."); print(filler1 * 2)
		
		# game condition three: defeat
		if (hand_sum > 21):
			games_lost += 1
			print(f"GAME OVER: You have won {games_won} and lost {games_lost} games of blackjack2."); print(filler1 * 2)

		# DO NOT FORGET TO UPDATE `game_count`
		game_count += 1
		with open('../blackjack/single_results.csv', 'a') as single_file:
			game_percent = games_won / game_count
			single_file.write(f'{game_count},{game_percent}\n')
		
	# store current results in next game iteration
	result = [name, games_won, games_lost]
	endgame_decision(result)


def endgame_decision(result):
	"""Prompts user to continue playing.

	If yes, game continues with past iterations results as input for
	next round of blackjack.

	If no, game ends. Results are written to separate file after which
	the user observes game statistics and line graph of winning
	percentage over time.
	"""

	prompt = input('Would you like to start a new game? yes or no\n> ')
	
	if prompt.lower() == 'yes':
		iterations = int(input('How many games would you like to play? Enter a number\n> '))
		simulation(result[0], result[1], result[2], iterations)
	
	if prompt.lower() == 'no':
		print(filler2 * 2); print("SCORE REPORT:"); print(filler1 * 2)
		print(f"Wins      : {result[1]}"); print(f"Losses    : {result[2]}"); print("Percentage: {:.4}".format(result[1] / (result[1] + result[2]))); print(filler2 * 2)
		with open('../blackjack/career_results.csv', 'a') as career_file:
			games_played = result[1] + result[2]
			win_percent = result[1] / games_played
			career_file.write('{},{:.4}\n'.format(games_played, win_percent))
			bj_analysis.convert_pd()
		with open('../blackjack/single_results.csv', 'w') as single_file:
			single_file.write('Game Count,Win Percentage\n')


if __name__ == '__main__':
	player = Player()
	iterations = int(input('How many games would you like to play? Enter a number\n> '))
	profile.run('simulation(player.name, player.games_won, player.games_lost, iterations)', 'restats.txt')