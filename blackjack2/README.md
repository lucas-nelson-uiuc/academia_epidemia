# README
Collection of python scripts that simulate games of blackjack2 and generate analyses of the game played.

![Screen Shot 2021-08-06 at 16 25 03](https://user-images.githubusercontent.com/78045025/128572602-dff3a42e-ac11-453c-a4c2-063820af0b74.png)

`blackjack2.py` simulates one game of blackjack2 using standard blackjack rules. However, the dealer always achieves a score of 20.5, so the only way to win
is by achieving a score of exactly 21. Win and loss totals are tracked and assigned to the user generated using the `Player()` class functionality. Multiple iterations can be played of various lengths one after the other, with a report from `bj_analysis.py` generated when play is stopped.

`bj_analysis.py` converts games into readable `pandas` DataFrames for data analysis. Since this game is meant to be played in terminal, graphing
functionality is limited to said environment using the `uniplot` package. This function is evoked in `blackjack2.py`.

![Screen Shot 2021-08-06 at 16 26 33](https://user-images.githubusercontent.com/78045025/128572688-da949788-8bc3-43bd-9999-896042a31e36.png)

`repetition.py` allows multiple cycles of `blackjack2.py` to be played. Rather than playing one cycle of 10,000 games using `blackjack2.py`, `repetition.py` allows
the user to play 10,000 games of blackjack2 10,000 times in one function call. Using a similar procedure to `bj_analysis.py`, a histogram is produced in the terminal displaying the sample's win percentage distribution.

![Screen Shot 2021-08-06 at 16 38 46](https://user-images.githubusercontent.com/78045025/128573636-eca2ee33-dbd0-4c59-99d4-f698a10a784f.png)

### Project Details
Author: Lucas Nelson

Completed: 07/08/2020

Updated: 07/04/2021
