# academia_epidemia

<b>Purpose</b> <br>
A collection of projects that stem from my curiosity and are curtailed for my consumption. Ordered from favorite to least favorite, but let me know if you disagree!

## Featured Projects

### 1. spotify_freemium
<i>In Progress</i><br>
Purpose: provide up-to-date, on-demand data analytics of a Spotify user's (mainly me) usage.

Procedure: using `spotipy` to access Spotify's API via user authentication tokens, I created a crawler that provides data per specified playlist. This data is gathered in a `pandas` DataFrame for further analysis.

Plans: correlation score (collect genre-specific playlists and measure correlation of audio features/analytics), comparison metrics (how much does one playlist correlate to a genre-representative playlist), flask application (user interface functionality; flask for familiarity but not limited to), and documentation (possibly packaging project).

### 2. newsPaper
<i>Completed: 01/05/2021<br></i>
Collection of Python, HTML, and CSS scripts that scrape, compile, and present information from various websites onto one HTML document for my consumption. Using Python libraries like `webbrowser`, `BeautifulSoup`, and `requests`, I scraped up-to-date information related to local weather forecasts, global politics, various sports leagues and their standings, <i>The History Channel</i>'s fact of the day, and much more. This script will write said information onto a file specific to that information before being manipulated on one final Python script that stitches the information into one final HTML document. The result is a webpage (designed via HTML, styled via CSS) that consistently provides updated information on what matters to me without the hassle of navigating multiple web pages nor at the risk of coming across distractions.

### 3. blackjack2
<i>Modified : 07/01/2021<br></i>
Simulation update. Included `repetition.py` to allow multiple cycles of n-iteration blackjack games to occur, complete with pandas DataFrame functionality and in-terminal graphing functions (line graph for winning percentage in `blackjack2.py` and histogram for winning distribution in `repetition.py`).

<i>Modified : 06/23/2021<br></i>
Massive revamp. Inclusion of `Player` class, `endgame_decision` function, manageable user interface and code readibility, timed performance using the `profile` package, and option to player `n > 1` games in one function call. Fun fact: printing is responsible for 40% of the time `blackjack2()` takes to execute.

<i>Completed: 07/26/2020<br></i>
Simple game of blackjack that follows basic principles. Prompts user to provide name and understanding of blackjack rules before gameplay. After gameplay starts, the user is dealt a card one-by-one until they either achieve a score of 21, a score greater than 21, or simply reject another card. Their final score is reported and the outcome of their game before being prompted to play again.

### 4. grade_calculator
<i>Completed: 12/06/2019<br></i>
Python script that returns my semester GPA. Completed by first inputting my list of classes per semester, categories (homework, midterms, projects, etc.) per class, and graded assignments per category. After computing a course's specific grade for all courses in a given semester, a stylized table is returned to display basic statistics about my performance.
