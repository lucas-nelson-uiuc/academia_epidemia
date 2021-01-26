#Import necessary libraries 
import webbrowser, requests, time, bs4

#Reddit information
with open('../raw/reddit.html', 'w') as reddit_brief:

    #Gather Reddit link
    reddit_URL = 'https://old.reddit.com/r/UIUC/new/'
    headers = {'User-Agent': 'Google Chrome'}

    #Gather HTML for specified Reddit page
    reddit_request = requests.get(reddit_URL, headers=headers)
    reddit_bs4 = bs4.BeautifulSoup(reddit_request.content, 'html.parser')

    #Parse by specific class and write to specified file
    reddit_title_div = reddit_bs4.select('p .title')
    for title in reddit_title_div:
        post_title = str(title)
        start_index = post_title.find(">")
        end_index = post_title.find("</a>")
        post_title = post_title[start_index + 1 : end_index]
        reddit_brief.write("==" + post_title + "--" + "\n")

#Phillies information
with open('../raw/phillies.html', 'w') as phillies_brief:
    
    phillies_URL = 'https://www.mlb.com/phillies'
    
    phillies_request = requests.get(phillies_URL)
    phillies_bs4 = bs4.BeautifulSoup(phillies_request.content, 'html.parser')

    phillies_title_list = []
    phillies_title_div = phillies_bs4.select('li .p-headline-stack__link')
    for title in phillies_title_div:
        post_title = str(title)
        start_index = post_title.find(">")
        end_index = post_title.find("</a>")
        post_title = post_title[start_index + 1 : end_index]
        phillies_title_list.append(post_title)

    i = 0
    while i < (len(phillies_title_list) / 2):
        phillies_brief.write("==" + phillies_title_list[i] + "--" + "\n")
        i += 1

#Redsox information
with open('../raw/redsox.html', 'w') as redsox_brief:

    redsox_URL = 'https://www.mlb.com/redsox'
    
    redsox_request = requests.get(redsox_URL)
    redsox_bs4 = bs4.BeautifulSoup(redsox_request.content, 'html.parser')

    redsox_title_list = []
    redsox_title_div = redsox_bs4.select('li .p-headline-stack__link')
    for title in redsox_title_div:
        post_title = str(title)
        start_index = post_title.find(">")
        end_index = post_title.find("</a>")
        post_title = post_title[start_index + 1 : end_index]
        redsox_title_list.append(post_title)

    i = 0
    while i < (len(redsox_title_list) / 2):
        redsox_brief.write("==" + redsox_title_list[i] + '--' + "\n")
        i += 1

#Weather information
with open('../raw/weather.html', 'w') as weather_brief:

    weather_URL = 'https://weather.com/weather/today/l/7a108c62bd14bf5335e5238972a5689b29c4bcc72d4648e20412bdc1d2aef8bf'

    weather_request = requests.get(weather_URL)
    weather_bs4 = bs4.BeautifulSoup(weather_request.content, 'html.parser')

    feels_like_div = weather_bs4.select('div .CurrentConditions--tempValue--3KcTQ')
    if True:
        feels_title = str(feels_like_div)
        start = feels_title.find(">")
        end = feels_title.find("</span>")
        feels_like = feels_title[start + 1 : end]
        weather_brief.write('Feels like: ' + "==" + feels_like + '--' + '\n')

    sunrise_div = weather_bs4.select('div .SunriseSunset--dateValue--2nwgx')
    if True:
        sunrise_title = str(sunrise_div)
        sunrise_start = sunrise_title.find(">")
        sunrise_end = sunrise_title.find("</p>")
        sunrise = sunrise_title[sunrise_start + 1 : sunrise_end]
        weather_brief.write('Sunrise: ' + "==" + sunrise + '--' + '\n')

    sunset_div = weather_bs4.select('div .SunriseSunset--dateValue--2nwgx')
    if True:
        sunset_title = str(sunset_div)
        separator = sunset_title.find(',')
        sunset_title2 = sunset_title[separator:]
        sunset_start = sunset_title2.find(">")
        sunset_end = sunset_title2.find("</p>")
        sunset = sunset_title2[sunset_start + 1 : sunset_end]
        weather_brief.write('Sunset: ' + "==" + sunset + '--' + '\n')

    moonphase_div = weather_bs4.select('div .WeatherDetailsListItem--wxData--23DP5')[-1]
    if True:
        moonphase_title = str(moonphase_div)
        moonphase_start = moonphase_title.find(">")
        moonphase_end = moonphase_title.find("</div>")
        moonphase = moonphase_title[moonphase_start + 1 : moonphase_end]
        weather_brief.write('Moonphase: ' + "==" + moonphase + '--' + '\n')

    precipitation_div = weather_bs4.select('div .CurrentConditions--precipValue--RBVJT')
    if precipitation_div != None:
        precipitation_title = str(precipitation_div)
        precipitation_start = precipitation_title.find("<span>")
        precipitation_end = precipitation_title.find("</span>")
        precipitation = precipitation_title[precipitation_start + 6 : precipitation_end]
        weather_brief.write('Precipitation: ' + "==" + precipitation + '--' + '\n')
    else:
        precipitation = '100'
        weather_brief.write('Precipitation: ' + "==" + precipitation + '--' + '\n')

#Cycling information
with open('../raw/cycling.html', 'w') as cycling_brief:

    #Cycling news
    cycling_news_URL = 'https://www.cyclingnews.com/news/'
    
    cycling_news_request = requests.get(cycling_news_URL)
    cycling_news_bs4 = bs4.BeautifulSoup(cycling_news_request.content, 'html.parser')

    cycling_news_div = cycling_news_bs4.select('div .article-name')
    cycling_brief.write('NEWS:\n')
    for title in cycling_news_div:
        post_title = str(title)
        start_index = post_title.find(">")
        end_index = post_title.find("</h3>")
        post = post_title[start_index + 1 : end_index]
        cycling_brief.write("==" + post + '--' + '\n')


    #Cycling results
    cycling_race_URL = 'https://www.cyclingnews.com/race-results/'

    cycling_race_request = requests.get(cycling_race_URL)
    cycling_race_bs4 = bs4.BeautifulSoup(cycling_race_request.content, 'html.parser')

    cycling_race_div = cycling_race_bs4.select('div .article-name')
    cycling_brief.write('RACES:\n')
    for title in cycling_race_div:
        post_title = str(title)
        start_index = post_title.find(">")
        end_index = post_title.find("</h3>")
        post = post_title[start_index + 1 : end_index]
        cycling_brief.write("==" + post + '--' + '\n')

#Manchester City information
with open('../raw/mancity.html', 'w') as mancity_brief:

    mancity_URL = 'https://www.mancity.com/fixtures'
    mancity_request = requests.get(mancity_URL)
    mancity_bs4 = bs4.BeautifulSoup(mancity_request.content, 'html.parser')

    mancity_date_div = mancity_bs4.select('div .fixture-header__competition-time')
    mancity_time_div = mancity_bs4.select('div .fixture-body__when-time')
    mancity_home_div = mancity_bs4.select('div .fixture-body__first-team-name')
    mancity_away_div = mancity_bs4.select('div .fixture-body__second-team-name')

    match_master_list = []

    for i in range(0, len(mancity_date_div)):
        if 'TBC' not in str(mancity_date_div[i]):

            date = str(mancity_date_div[i])
            date_start = date.find(">")
            date_end = date.find("</time>")
            match_date = date[date_start + len(">") : date_end]
            match_date = match_date.lstrip()
            match_date = match_date.rstrip()

            time = str(mancity_time_div[i])
            time_start = time.find(">")
            time_end = time.find("</time>")
            match_time = time[time_start + len(">") : time_end]
            match_time = match_time.lstrip()
            match_time = match_time.rstrip()

            home = str(mancity_home_div[i])
            home_start = home.find('<span class="shown-lg">')
            home_end = home.find("</span>")
            match_home = home[home_start + len('<span class="shown-lg">') : home_end]
            match_home = match_home.lstrip()
            match_home = match_home.rstrip()
            
            away = str(mancity_away_div[i])
            away_start = away.find('<span class="shown-lg">')
            away_end = away.find("</span>")
            match_away = away[away_start + len('<span class="shown-lg">') : away_end]
            match_away = match_away.lstrip()
            match_away = match_away.rstrip()

            match_details = [match_date, match_time, match_home, match_away]
            match_master_list.append(match_details)


    for match in match_master_list:
        paste_string = ''
        for detail in range(0, len(match) - 1):
            paste_string += f'{match[detail]}---'
        paste_string += f'{match[3]}' + '\n'
        mancity_brief.write(paste_string)

#ECNMST, MLB (news) information
with open('../raw/nytimes.html', 'w') as nytimes_brief:

    #collect three stories:
    #header1(international tab @ The Economist)
    #header2(europe tab @ The Economist)
    #side1(economics tab @ The Economist)
    #side2(sports tab @ MLB)
    newspaper_list = []
    
    #bs4 for HEADER1(INTERNATIONAL)
    international_URL = 'https://www.economist.com/international/'
    international_request = requests.get(international_URL)
    international_bs4 = bs4.BeautifulSoup(international_request.content, 'html.parser')
    international = international_bs4.select('div .headline-link')

    ###strip for HEADER1
    i = 0
    prior = 0
    posterior = 0
    
    while i < 4:
        header_string = str(international)[prior : ]
        end_of_headline = header_string.find(', ')
        headline = header_string[ : end_of_headline]

        open_tag = '<span class="teaser__headline teaser__headline--sc3">'
        close_tag = '</span></a>'
        header_start = header_string.find(open_tag)
        header_end = header_string.find(close_tag)
        newspaper_header = header_string[header_start + len(open_tag) : header_end]

        if (newspaper_header != '') and (newspaper_header != None) and (len(newspaper_header) > 10):
            newspaper_list.append(newspaper_header)
            i += 1
        
        prior += end_of_headline + len(', ')

    #bs4 for HEADER2(EUROPE)
    europe_URL = 'https://www.economist.com/europe/'
    europe_request = requests.get(europe_URL)
    europe_bs4 = bs4.BeautifulSoup(europe_request.content, 'html.parser')
    europe = europe_bs4.select('div .headline-link')

    ###strip for HEADER2
    i = 0
    prior = 0
    posterior = 0
    
    while i < 5:
        header_string = str(europe)[prior : ]
        end_of_headline = header_string.find(', ')
        headline = header_string[ : end_of_headline]

        open_tag = '<span class="teaser__headline teaser__headline--sc3">'
        close_tag = '</span></a>'
        header_start = header_string.find(open_tag)
        header_end = header_string.find(close_tag)
        newspaper_header = header_string[header_start + len(open_tag) : header_end]

        if (newspaper_header != '') and (newspaper_header != None) and (len(newspaper_header) > 10):
            newspaper_list.append(newspaper_header)
            i += 1
        
        prior += end_of_headline + len(', ')

    #bs4 for SIDE1(ECONOMICS)
    econ_side1_URL = 'https://www.economist.com/finance-and-economics/'
    econ_side1_request = requests.get(econ_side1_URL)
    econ_side1_bs4 = bs4.BeautifulSoup(econ_side1_request.content, 'html.parser')
    econ_side1 = econ_side1_bs4.select('div .headline-link')

    ###strip for SIDE1
    i = 0
    prior = 0
    posterior = 0
    
    while i < 5:
        side2 = str(econ_side1)[prior : ]
        end_of_headline = side2.find(', ')
        headline = side2[ : end_of_headline]

        open_tag = '<span class="teaser__headline teaser__headline--sc3">'
        close_tag = '</span></a>'
        side2_start = side2.find(open_tag)
        side2_end = side2.find(close_tag)
        newspaper_side2 = side2[side2_start + len(open_tag) : side2_end]

        if (newspaper_side2 != '') and (newspaper_side2 != None) and (len(newspaper_side2) > 10):
            newspaper_list.append(newspaper_side2)
            i += 1

        prior += end_of_headline + len(', ')


    #bs4 for SIDE2(SPORTS)
    mlb_side2_URL = 'https://www.mlb.com/news'
    mlb_side2_request = requests.get(mlb_side2_URL)
    mlb_side2_bs4 = bs4.BeautifulSoup(mlb_side2_request.content, 'html.parser')
    mlb_side2 = mlb_side2_bs4.select('div .article-navigation__item__meta-headline')

    ###strip for SIDE2
    for i in range(0, 5):
        article = str(mlb_side2[i])
        article_start = article.find('>')
        article_end = article.find('</span>')
        newspaper_article = article[article_start + len('>') : article_end]
        newspaper_article = newspaper_article.lstrip()
        newspaper_article = newspaper_article.rstrip()
        newspaper_list.append(newspaper_article)

    #attach to file
    for headline in newspaper_list:
        headline += '\n'
        nytimes_brief.write(headline)

#PREM_LEG information
with open('../raw/pl_scorecard.html', 'w') as scorecard_brief:

    pl_URL = 'https://www.skysports.com/premier-league-table'
    pl_request = requests.get(pl_URL)
    pl_bs4 = bs4.BeautifulSoup(pl_request.content, 'html.parser')
    
    pl_team = pl_bs4.select('div .standing-table__cell--name-link')
    pl_data = pl_bs4.select('tbody .standing-table__row')
    
    team_list = []
    i = 0
    for team in pl_team[0:5]:

        team = str(team)
        team_start = team.find('>')
        team_end = team.find('</a>')
        team_name = team[team_start + len('>') : team_end]

        team_details = []
        team_details.append(team_name)
        
        data = str(pl_data[i])
        
        #TEAM ROW
        team_data_start = data.find('</a>')
        team_data_end = data.find('<td class="standing-table__cell is-hidden--bp15 is-hidden--bp35"')
        team_data_row = data[team_data_start + len('</a>') : team_data_end]
        teamteam = team_data_row.split('\n')

        #POINTS
        team_points_raw = teamteam[9]
        team_points_start = team_points_raw.find('>')
        team_points_end = team_points_raw.find('</td>')
        team_points = team_points_raw[team_points_start + len('>') : team_points_end]
        team_details.append(team_points)

        #GAMES PLAYED
        team_games_raw = teamteam[2]
        team_games_start = team_games_raw.find('>')
        team_games_end = team_games_raw.find('</td>')
        team_games = team_games_raw[team_games_start + len('>') : team_games_end]
        team_details.append(team_games)

        #WINS
        team_wins_raw = teamteam[3]
        team_wins_start = team_wins_raw.find('>')
        team_wins_end = team_wins_raw.find('</td>')
        team_wins = team_wins_raw[team_wins_start + len('>') : team_wins_end]
        team_details.append(team_wins)

        #DRAWS
        team_draws_raw = teamteam[4]
        team_draws_start = team_draws_raw.find('>')
        team_draws_end = team_draws_raw.find('</td>')
        team_draws = team_draws_raw[team_draws_start + len('>') : team_draws_end]
        team_details.append(team_draws)

        #LOSSES
        team_losses_raw = teamteam[5]
        team_losses_start = team_losses_raw.find('>')
        team_losses_end = team_losses_raw.find('</td>')
        team_losses = team_losses_raw[team_losses_start + len('>') : team_losses_end]
        team_details.append(team_losses)

        #APPEND
        team_list.append(team_details)
        
        #UPDATE
        i += 1



    for team in team_list:
        if team[0] == 'Manchester United':
            team[0] = 'MUN'
        if team[0] == 'Liverpool':
            team[0] = 'LIV'
        if team[0] == 'Leicester City':
            team[0] = 'LEI'
        if team[0] == 'Everton':
            team[0] = 'EVE'
        if team[0] == 'Tottenham Hotspur':
            team[0] = 'TOT'
        if team[0] == 'Manchester City':
            team[0] = 'MCI'
        if team[0] == 'Southampton':
            team[0] = 'SOU'
        if team[0] == 'Aston Villa':
            team[0] = 'AVL'
        if team[0] == 'Chelsea':
            team[0] = 'CHE'
        if team[0] == 'West Ham United':
            team[0] = 'WHU'
        if team[0] == 'Arsenal':
            team[0] = 'ARS'
        if team[0] == 'Leeds United':
            team[0] = 'LED'
        if team[0] == 'Crystal Palace':
            team[0] = 'CRY'
        if team[0] == 'Wolverhampton Wanderers':
            team[0] = 'WOL'
        if team[0] == 'Newcastle United':
            team[0] = 'NEW'
        if team[0] == 'Burnley':
            team[0] = 'BUR'
        if team[0] == 'Brighton and Hove Albion':
            team[0] = 'BHA'
        if team[0] == 'Fulham':
            team[0] = 'FFC'
        if team[0] == 'West Bromwich Albion':
            team[0] = 'WBA'
        if team[0] == 'Sheffield United':
            team[0] = 'SHU'

    final_list = []
    for team in team_list:
        team = '...'.join(team)
        team += '\n'
        final_list.append(team)

    for team in final_list:
        scorecard_brief.write(team)
        
#NCAAM information
with open('../raw/ncaam_scorecard.html', 'w') as scorecard_brief:

    ncaam_URL = 'https://www.sports-reference.com/cbb/conferences/big-ten/2021.html'
    ncaam_request = requests.get(ncaam_URL)
    ncaam_bs4 = bs4.BeautifulSoup(ncaam_request.content, 'html.parser')

    ncaam_team = ncaam_bs4.select('div .left')
    
    b1g_schools = ['Michigan', 'Iowa', 'Wisconsin', 'Illinois', 'Ohio State', 
        'Indiana', 'Purdue', 'Northwestern', 'Minnesota', 'Rutgers',
        'Michigan State', 'Maryland', 'Penn State', 'Nebraska']
    
    team_names = []
    for team in ncaam_team:
        if '<td class="left" data-stat="school_name">' in str(team):
            team = str(team)
            team_open_tag = '<td class="left" data-stat="school_name">'
            team_start = team[len(team_open_tag) + 1:].find('>')
            team_start = len(team_open_tag) + team_start
            team_end = team.find('</a>')
            team_name = team[team_start + 2: team_end]
            team_names.append(team_name)

    newspaper_names = []
    for i in range(0, 5):
        newspaper_names.append(team_names[i])
    
    for i in range(0, 5):
        if newspaper_names[i] == 'Michigan':
            newspaper_names[i] = 'MICH'
        if newspaper_names[i] == 'Iowa':
            newspaper_names[i] = 'IOWA'
        if newspaper_names[i] == 'Wisconsin':
            newspaper_names[i] = 'WISC'
        if newspaper_names[i] == 'Illinois':
            newspaper_names[i] = 'ILL'
        if newspaper_names[i] == 'Ohio State':
            newspaper_names[i] = 'OSU'
        if newspaper_names[i] == 'Indiana':
            newspaper_names[i] = 'IND'
        if newspaper_names[i] == 'Purdue':
            newspaper_names[i] = 'PUR'
        if newspaper_names[i] == 'Northwestern':
            newspaper_names[i] = 'NU'
        if newspaper_names[i] == 'Minnesota':
            newspaper_names[i] = 'MINN'
        if newspaper_names[i] == 'Rutgers':
            newspaper_names[i] = 'RUT'
        if newspaper_names[i] == 'Michigan State':
            newspaper_names[i] = 'MSU'
        if newspaper_names[i] == 'Maryland':
            newspaper_names[i] = 'MARY'
        if newspaper_names[i] == 'Penn state':
            newspaper_names[i] = 'PSU'
        if newspaper_names[i] == 'Nebraska':
            newspaper_names[i] = 'NEB'

    
    ncaam_team_div = ncaam_bs4.find(id='div_standings')
    ncaam_team_div = str(ncaam_team_div)
    ncaam_team_otbody = ncaam_team_div.find('<tbody>')
    ncaam_team_ctbody = ncaam_team_div.find('</tbody>')
    ncaam_team_table = ncaam_team_div[ncaam_team_otbody : ncaam_team_ctbody]

    team_details = []
    ncaam_team_rows = ncaam_team_table.split('</tr>')

    for i in range(0, 5):
        team_data = str(ncaam_team_rows[i])
        data_entries = team_data.split('</td>')
        
        team_wins_raw = data_entries[4]
        team_wins_start = team_wins_raw.find('>')
        team_wins = team_wins_raw[team_wins_start + 1 : ]

        team_loss_raw = data_entries[5]
        team_loss_start = team_loss_raw.find('>')
        team_loss = team_loss_raw[team_loss_start + 1 : ]

        team_pct_raw = data_entries[6]
        team_pct_start = team_pct_raw.find('>')
        team_pct = team_pct_raw[team_pct_start + 1 : ]

        team_tPPG_raw = data_entries[7]
        team_tPPG_start = team_tPPG_raw.find('>')
        team_tPPG = team_tPPG_raw[team_tPPG_start + 1 : ]

        team_oPPG_raw = data_entries[8]
        team_0PPG_start = team_oPPG_raw.find('>')
        team_0PPG = team_oPPG_raw[team_0PPG_start + 1 : ]

        team_name = newspaper_names[i]

        final_team_data = f'{team_name}...{team_wins}...{team_loss}...{team_pct}...{team_tPPG}...{team_0PPG}'
        team_details.append(final_team_data)

    for row in team_details:
        final_stat_line = row + '\n'
        scorecard_brief.write(final_stat_line)

#MLB standings
with open('../raw/mlb_scorecard.html', 'w') as mlb_scorecard:

    mlb_URL = 'https://www.baseball-reference.com/leagues/NL/2020-standings.shtml'
    mlb_request = requests.get(mlb_URL)
    mlb_bs4 = bs4.BeautifulSoup(mlb_request.content, 'html.parser')

    #collect team details
    team_details = []

    #gather team name
    mlb_team = mlb_bs4.select('div .left')
    for i in range(0, 5):
        team = str(mlb_team[i])
        team_end = team.find('</a>')
        team_update = team[:team_end]
        team_start = team_update.rfind('>')
        team_name = team_update[team_start + len('>'):]
        
        if team_name == 'Atlanta Braves':
            team_name = 'ATL'
        if team_name == 'Miami Marlins':
            team_name = 'MIA'
        if team_name == 'Philadelphia Phillies':
            team_name = 'PHI'
        if team_name == 'New York Mets':
            team_name = 'NYM'
        if team_name == 'Washington Nationals':
            team_name = 'WAS'

        team_details.append(team_name)

    mlb_content = str(mlb_bs4)
    mlb_rows = mlb_content.split('<tr >')
    nleast_rows = mlb_rows[1:6]
    
    #remove extra HTML at end of last standing
    last_place = nleast_rows[4]
    last_place_end = last_place.find('<tr class="league_average_table" >')
    last = last_place[:last_place_end]
    last = last.rstrip()
    nleast_rows[4] = last
    
    #gather team data
    for row in nleast_rows:
        if '</a></strong></td>' in row:
            row_start = row.find('</a></strong></td>')
            row_end = row.find('<td class="right " data-stat="record_last_30"')
            team_row = row[row_start + len('</a></strong></td>') : row_end]
            team_data = team_row.split('</td>')

        else:
            row_start = row.find('</a></td>')
            row_end = row.find('<td class="right " data-stat="record_last_30"')
            team_row = row[row_start + len('</a></td>') : row_end]
            team_data = team_row.split('</td>')

        #wins
        team_wins = team_data[0]
        
        if '<strong>' in team_wins:
            final_wins = team_wins[len('<td class="right " data-stat="W" ><strong>') : team_wins.rfind('<')]

        else:
            final_wins = team_wins[len('<td class="right " data-stat="W" >') : ]

        #losses
        team_loss = team_data[1]
        
        if '<strong>' in team_loss:
            final_loss = team_loss[len('<td class="right " data-stat="L" ><strong>') : team_loss.rfind('<')]

        else:
            final_loss = team_loss[len('<td class="right " data-stat="L" >') : ]

        #rdiff
        team_rdiff = team_data[8]
        
        if '<strong>' in team_rdiff:
            final_rdiff = team_rdiff[len('<td class="right " data-stat="run_diff" ><strong>') : team_rdiff.rfind('<')]

        else:
            final_rdiff = team_rdiff[len('<td class="right " data-stat="run_diff" >') : ]

        #pythW
        team_pythW = team_data[11]
        team_pythW = team_pythW[len('<td class="right " data-stat="record_pythag" ') : ]
        
        if '<strong>' in team_rdiff:
            pythW_start = team_pythW.find('<strong>')
            pythW_end = team_pythW.find('</strong>')
            raw_pythW = team_pythW[pythW_start + len('<strong>') : pythW_end]
            final_pythW = raw_pythW[ : raw_pythW.find('-')]

        else:
            raw_pythW = team_pythW[team_pythW.find('>') + len('>'): ]
            final_pythW = raw_pythW[ : raw_pythW.find('-')]

        #last20
        team_last20 = team_data[26]
        team_last20 = team_last20[len('<td class="right " data-stat="record_last_10" ') : ]
        
        if '<strong>' in team_rdiff:
            last20_start = team_last20.find('<strong>')
            last20_end = team_last20.find('</strong>')
            raw_last20 = team_last20[last20_start + len('<strong>') : last20_end]
            final_last20 = raw_last20[ : raw_last20.find('-')]

        else:
            raw_last20 = team_last20[team_last20.find('>') + len('>'): ]
            final_last20 = raw_last20[ : raw_last20.find('-')]

        final_team_data = [final_wins, final_loss, final_rdiff, final_pythW, final_last20]

        team_details.append(final_team_data)

    #rearrange data
    for i in range(0, 5):
        for data in team_details[i + 5]:
            team_details[i] += '---' + data
    team_details = team_details[0:5]

    #write to file
    for team in team_details:
        mlb_scorecard.write(team + '\n')

#History (OTD)
with open('../raw/history.html', 'w') as history_brief:

    history_URL = 'https://www.history.com/this-day-in-history'
    history_request = requests.get(history_URL)
    history_bs4 = bs4.BeautifulSoup(history_request.content, 'html.parser')
    
    #gather header, paragraphs
    newspaper_history = []
    
    #header
    history_h1 = history_bs4.select('div .m-detail-header--title')
    history_header = str(history_h1)
    history_header_start = history_header.find('>')
    history_header_end = history_header.find('</h1>')
    newspaper_header = history_header[history_header_start + len('>') : history_header_end]

    newspaper_history.append(newspaper_header) 

    #paragraphs
    history_p = history_bs4.select('div .m-detail--body')
    history_paragraph = str(history_p)
    history_paragraphs = history_paragraph.split('</p>')
    for paragraph in history_paragraphs:
        if not(('WATCH' in paragraph) or ('READ MORE' in paragraph) or (paragraph == history_paragraphs[-1])):
            paragraph_start = paragraph.find('<p>')
            paragraph_end = paragraph.find('</p>')
            paragraph = paragraph[paragraph_start + len('<p>') : paragraph_end]
            newspaper_history.append(paragraph)

    for element in newspaper_history:
        element += '\n'
        history_brief.write(element)

#Fangraphs (Community)
with open('../raw/fangraphs.html', 'w') as fangraphs_brief:

    fg_URL = 'https://community.fangraphs.com/'
    fg_request = requests.get(fg_URL)
    fg_bs4 = bs4.BeautifulSoup(fg_request.content, 'html.parser')

    newspaper_list = []
    
    #article_title
    article_title = str(fg_bs4.find(class_='posttitle'))
    title_end = article_title.find('</a></h2>')
    article_update = article_title[ : title_end]
    title_start = article_update.rfind('>')
    newspaper_title = article_update[title_start + len('>') : ]
    newspaper_list.append(newspaper_title)

    #article_paragraphs
    article_paragraphs = str(fg_bs4.find(class_='fullpostentry'))
    paragraphs_list = article_paragraphs.split('<p>')
    
    for paragraph in paragraphs_list[1:]:
        paragraph_end = paragraph.rfind('</p>')
        paragraph = paragraph[ : paragraph_end]
        newspaper_list.append(paragraph)

    for element in newspaper_list:
        fangraphs_brief.write(element + '\n')

#NASA article
with open('../raw/nasa.html', 'w') as nasa_brief:

    nasa_URL = 'https://blogs.nasa.gov/'
    nasa_request = requests.get(nasa_URL)
    nasa_bs4 = bs4.BeautifulSoup(nasa_request.content, 'html.parser')

    #collect article information
    article_list = []
    
    #title of article
    article_title = nasa_bs4.find(class_='entry-title')
    title = str(article_title)
    title_end = str(article_title).rfind('</a></h2>')
    title_update = title[ : title_end]
    title_start = title_update.rfind('>')
    final_title = title_update[title_start + len('>') : ]

    article_list.append(final_title)

    #content of article on front page (not final)
    article_content = nasa_bs4.find(class_='entry-content')
    link = str(article_content)
    link_start = link.find('<a href="')
    link_update = link[link_start + len('<a href="') : ]
    link_end = link_update.find('">')
    final_link = link_update[ : link_end]
    
    #content of article
    nasa2_URL = final_link
    nasa2_request = requests.get(nasa2_URL)
    nasa2_bs4 = bs4.BeautifulSoup(nasa2_request.content, 'html.parser')

    main_content = nasa2_bs4.find(class_= 'entry-content')
    main_paragraphs = str(main_content).split('<p>')
    for paragraph in main_paragraphs[1:]:
        paragraph_end = paragraph.find('</p>')
        paragraph = paragraph[ : paragraph_end]
        paragraph = paragraph.lstrip()
        paragraph = paragraph.rstrip()
        if 'iframe' not in paragraph:
            article_list.append(paragraph)

    article_paragraphs = '<br><br>'.join(article_list[1:])
    final_list = [article_list[0], article_paragraphs]
    
    for elem in final_list:
        nasa_brief.write(elem + '\n')




