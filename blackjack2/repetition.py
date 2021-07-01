# Simulation of blackjack with terminal and graphing functionality.
# Contains multiple points of user input and file writing, but is
# kept within a controlled environment for no user interference.

import profile
import random
import pandas as pd
import uniplot

import blackjack2
import bj_analysis


class Player:

	def __init__(self):
		self.name = 'Lucas'
		self.games_won  = 0


def repetition(player, iterations, cycles):
	"""Simulates cycles of blackjack games at specified iterations.

	Tracks player performance over time and updates separate file
	per cycle of recent n-iterations' performance.
	"""

	deck = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7,
			'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':[1, 11]}
	cycle_count = 1

	while (cycle_count < cycles + 1):

		print('CYCLE COUNT: {}'.format(cycle_count))

		iteration_count = 1
		games_won = 0
		while (iteration_count < iterations + 1):

			hand_sum = 0
			while (hand_sum < 21):
			
				dealt_card = random.choice(list(deck.keys()))

				if (dealt_card == "ace"):
					if hand_sum + 11 > 21:
						hand_sum += deck[dealt_card][0]
					else:
						hand_sum += deck[dealt_card][1]

				if (dealt_card != 'ace'):
					hand_sum += deck[dealt_card]
				
				# game condition one: undetermined
				if (hand_sum < 21):
					continue

			# game condition two: success
			if (hand_sum == 21):
				games_won += 1

			# DO NOT FORGET TO UPDATE `iteration_count`
			iteration_result = [iteration_count, games_won, games_won / iteration_count]
			iteration_count += 1

		cycle_results = [cycle_count,iteration_count - 1,iteration_result[1],iteration_result[2]]
		print('iterations: {}\ngames won : {}\nwin percentage: {}'.format(cycle_results[1], cycle_results[2], cycle_results[3]))
		with open('../blackjack/repetition_results.csv', 'a') as rep_file:
			cycle_results = [str(elem) for elem in cycle_results]
			cycle_string = ','.join(cycle_results)
			rep_file.write(cycle_string + '\n')
		cycle_count += 1

def hist_results(file='../blackjack/repetition_results.csv'):
	df = pd.read_csv(file, names = ['cycle_num', 'iters', 'games_won', 'win_pct'])
	print(df)
	uniplot.histogram(df['win_pct'])
	with open('../blackjack/repetition_results.csv', 'w') as rep_file:
		rep_file.write('')

if __name__ == '__main__':
	player = Player()
	
	iterations = int(input("{:16}: ".format("Enter iterations")))
	cycles = int(input("{:16}: ".format("Enter cycles")))
	
	repetition(player, iterations, cycles)
	hist_results()