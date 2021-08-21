# academia_epidemia

<b>Purpose</b> <br>
A collection of projects that stem from my curiosity and are curtailed for my consumption. Ordered from favorite to least favorite, but let me know if you disagree!

## Featured Projects

### 1. newsPaper
<i>Completed: 01/05/2021<br></i>
Collection of Python, HTML, and CSS scripts that scrape, compile, and present information from various websites onto one HTML document for my consumption. Using Python libraries like `webbrowser`, `BeautifulSoup`, and `requests`, I scraped up-to-date information related to local weather forecasts, global politics, various sports leagues and their standings, <i>The History Channel</i>'s fact of the day, and much more. This script will write said information onto a file specific to that information before being manipulated on one final Python script that stitches the information into one final HTML document. The result is a webpage (designed via HTML, styled via CSS) that consistently provides updated information on what matters to me without the hassle of navigating multiple web pages nor at the risk of coming across distractions.

### 2. blackjack2
<i>Modified : 07/01/2021<br></i>
Simulation update. Included `repetition.py` to allow multiple cycles of n-iteration blackjack games to occur, complete with pandas DataFrame functionality and in-terminal graphing functions (line graph for winning percentage in `blackjack2.py` and histogram for winning distribution in `repetition.py`).

<i>Modified : 06/23/2021<br></i>
Massive revamp. Inclusion of `Player` class, `endgame_decision` function, manageable user interface and code readibility, timed performance using the `profile` package, and option to player `n > 1` games in one function call. Fun fact: printing is responsible for 40% of the time `blackjack2()` takes to execute.

<i>Completed: 07/26/2020<br></i>
Simple game of blackjack that follows basic principles. Prompts user to provide name and understanding of blackjack rules before gameplay. After gameplay starts, the user is dealt a card one-by-one until they either achieve a score of 21, a score greater than 21, or simply reject another card. Their final score is reported and the outcome of their game before being prompted to play again.

### 3. grade_calculator

<i>Modified : 06/23/2021<br></i>
Massive revamp. Greater inclusion of `Student()` class and implementation of more single purpose functions. Allows for a much smoother and easy-to-follow experience for the user in the terminal with a nicely plotted table detailing the student's performance in the requested semester.


<i>Completed: 12/06/2019<br></i>
Python script that returns my semester GPA. Completed by first inputting my list of classes per semester, categories (homework, midterms, projects, etc.) per class, and graded assignments per category. After computing a course's specific grade for all courses in a given semester, a stylized table is returned to display basic statistics about my performance.

### 4. password_manager
<i>Completed: 08/21/2021<br></i>
`Tkinter` GUI that encrypts and decrypts passwords for a provided account(s). Interface is simple to use and information is kept secret in a stored text file.
