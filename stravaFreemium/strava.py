import bs4
import webbrowser
import requests

strava_URL = 'https://www.strava.com/dashboard?feed_type=my_activity'
strava_request = requests.get(strava_URL)
strava_bs4 = bs4.BeautifulSoup(strava_request.content, 'html.parser')

strava_activites = strava_bs4.find_all('div')
print(strava_activites)