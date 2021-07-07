# README
Collection of python scripts that simulate games of blackjack2 and generate analyses of the game played.

`blackjack2.py` simulates one game of blackjack2 using standard blackjack rules. However, the dealer always achieves a score of 20.5, so the only way to win
is by achieving a score of exactly 21. Win and loss totals are tracked and assigned to the user generated using the `Player()` class functionality. Multiple iterations
can be played of various lengths one after the other, with a report from `bj_analysis.py` generated when play is stopped.

`bj_analysis.py` converts games into readable `pandas` DataFrames for data analysis. Since this game is meant to be played in terminal, graphing
functionality is limited to said environment using the `uniplot` package. This function is evoked in `blackjack2.py`.

`repetition.py` allows multiple cycles of `blackjack2.py` to be played. Rather than playing one cycle of 10,000 games using `blackjack2.py`, `repetition.py` allows
the user to play 10,000 games of blackjack2 10,000 times in one function call. Using a similar procedure to `bj_analysis.py`, a histogram is produced in the terminal
displaying the sample's win percentage distribution.
