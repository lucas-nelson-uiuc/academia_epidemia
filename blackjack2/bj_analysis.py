import pandas as pd
import numpy as np
import uniplot

def convert_pd():
    with open('../blackjack/single_results.csv', 'r') as results_file:
        df = pd.read_csv(results_file, delimiter=',')
        uniplot.plot(df['Win Percentage'], color=True, y_max=1, y_min=0)

if __name__ == '__main__':
    convert_pd()