import webbrowser
from datetime import date
import time
import calendar


### forecast tab
with open('../raw/weather.html', 'r') as forecast_file:
    forecast = forecast_file.readlines()
    i = 0
    
    for data in forecast:
        start_index = data.find("==")
        end_index = data.find("--")
        return_string = data[start_index + 2 : end_index]
        forecast[i] = return_string
        i += 1

    temperature = forecast[0]
    sunrise = forecast[1]
    sunset = forecast[2]
    moonphase = forecast[3]
    precipitation = forecast[4]
    precipitation = precipitation[ : precipitation.find('%')]

    ### date tab
    today = date.today()
    day_of_week = calendar.day_name[today.weekday()]
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

###headline image
if day_of_week == 'Sunday':
    headline_image = '../images/switzerland_01.jpg'

if day_of_week == 'Monday':
    headline_image ='../images/switzerland_02.jpg'

if day_of_week == 'Tuesday':
    headline_image ='../images/switzerland_03.jpeg'

if day_of_week == 'Wednesday':
    headline_image ='../images/switzerland_04.jpg'

if day_of_week == 'Thursday':
    headline_image ='../images/switzerland_05.jpeg'

if day_of_week == 'Friday':
    headline_image ='../images/switzerland_06.jpg'

if day_of_week == 'Saturday':
    headline_image ='../images/switzerland_07.jpg'

###headline stories
with open('../raw/nytimes.html', 'r') as nytimes:
    headlines = nytimes.readlines()

    headlines_list = []
    for headline in headlines:
        headline = headline[:-1]
        headlines_list.append(headline)

###premier league table
with open('../raw/pl_scorecard.html') as pl_brief:
    table_rows = pl_brief.readlines()
    
    pl_table_rows = []
    for row in table_rows:
        row = row[:-1]
        row = row.split('...')
        pl_table_rows.append(row)

###mlb standings
with open('../raw/mlb_scorecard.html') as mlb_brief:
    table_rows = mlb_brief.readlines()
    
    mlb_table_rows = []
    for row in table_rows:
        row = row[:-1]
        row = row.split('---')
        mlb_table_rows.append(row)

###ncaam standings
with open('../raw/ncaam_scorecard.html') as ncaam_brief:
    table_rows = ncaam_brief.readlines()
    
    ncaam_table_rows = []
    for row in table_rows:
        row = row[:-1]
        row = row.split('...')
        ncaam_table_rows.append(row)
            
###fangraphs community
with open('../raw/fangraphs.html', 'r') as fangraphs_brief:
    fangraphs_elements = fangraphs_brief.readlines()

    fangraphs_list = []
    for element in fangraphs_elements:
        element = element[:-1]
        element = element.rstrip()
        element = element.lstrip()
        fangraphs_list.append(element)
    
    fangraphs_paragraph = '<br><br>'.join(fangraphs_list[1:len(fangraphs_list)])
    final_fangraphs_list = [fangraphs_list[0], fangraphs_paragraph]

###nasa article
with open('../raw/nasa.html', 'r') as nasa_brief:
    nasa_elements = nasa_brief.readlines()

    nasa_list = []
    for element in nasa_elements:
        element = element.lstrip()
        element = element.rstrip()
        nasa_list.append(element)

###history OTD
with open('../raw/history.html', 'r') as history_brief:
    history_facts = history_brief.readlines()

    history_list = []
    for fact in history_facts:
        fact = fact.lstrip()
        fact = fact.rstrip()
        history_list.append(fact)
    
    history_paragraph = '.<br><br>'.join(history_list[1:len(history_list)])
    final_history_list = [history_list[0], history_paragraph]


html_script = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>REAL WEBSITE</title>
    <link rel="stylesheet" href="../css/newspaper.css">
    <link rel="shortcut icon" type="image/png" href="../images/digBeta.png">
</head>
<body>
    
    <div class="navigation_bar">
        <div class="left_nav">
             <p>Temperature</p>
             <p>{temperature} F | {precipitation}% rain</p>
             <p>{moonphase}</p>
             <p>{sunrise} | {sunset}</p>
        </div>
        <div class="center_nav">
            <a href="../reuben/newspaper.html">Academia Epidemia</a>
        </div>
        <div class="right_nav">
            <h6>{day_of_week}</h6>
            <h6>{today}</h6>
            <h6>{current_time}</h6>
        </div>
    </div>
    
    <div class="sections_tab">
        <a href="../reuben/univ_illinois.html">University of Illinois</a>
        <a href="../reuben/newspaper.html">Stats News & Econ News</a>
        <a href="../reuben/newspaper.html">European Sports</a>
        <a href="../reuben/newspaper.html">American Sports</a>
        <a href="../reuben/newspaper.html">Research</a>
        <a href="../reuben/newspaper.html">r/lou.nel</a>
        <a href="../reuben/newspaper.html">Weekend</a>
    </div>
    
    <div class="wrapper">
        <div class="headline">
            <div class='headline_image'>
                <img src='{headline_image}' alt='Switzerland'>
            </div>
        
            <div class="headline_story">
                <div class="story1">
                    <h2>International Politics</h2>
                    <p>* {headlines_list[0]}</p>
                    <p>* {headlines_list[1]}</p>
                    <p>* {headlines_list[2]}</p>
                    <p>* {headlines_list[3]}</p>
                </div>
                <div class="story2">
                    <h2>European Governments</h2>
                    <p>* {headlines_list[4]}</p>
                    <p>* {headlines_list[5]}</p>
                    <p>* {headlines_list[6]}</p>
                    <p>* {headlines_list[7]}</p>
                    <p>* {headlines_list[8]}</p>
                </div>
                <div class="story3">
                    <h2>Economic Forecasts</h2>
                    <p>* {headlines_list[9]}</p>
                    <p>* {headlines_list[10]}</p>
                    <p>* {headlines_list[11]}</p>
                    <p>* {headlines_list[12]}</p>
                    <p>* {headlines_list[13]}</p>
                </div>
                <div class="story4">
                    <h2>Major League Baseball</h2>
                    <p>* {headlines_list[14]}</p>
                    <p>* {headlines_list[15]}</p>
                    <p>* {headlines_list[16]}</p>
                    <p>* {headlines_list[17]}</p>
                    <p>* {headlines_list[18]}</p>
                </div>
            </div>
        </div>

        <div class="main_content">
            <div class="left_content">
                <div class="prem_leg">
                    <h3>Premier League Table</h3>
                    <div class="prem_leg_grid">
                        <div class="prem_leg_col1">
                            <i>.</i><p>{pl_table_rows[0][0]}</p><p>{pl_table_rows[1][0]}</p><p>{pl_table_rows[2][0]}</p><p>{pl_table_rows[3][0]}</p><p>{pl_table_rows[4][0]}</p>
                        </div>
                        <div class="prem_leg_col2">
                            <b>PTS</b><p>{pl_table_rows[0][1]}</p><p>{pl_table_rows[1][1]}</p><p>{pl_table_rows[2][1]}</p><p>{pl_table_rows[3][1]}</p><p>{pl_table_rows[4][1]}</p>
                        </div>
                        <div class="prem_leg_col3">
                            <b>GP</b><p>{pl_table_rows[0][2]}</p><p>{pl_table_rows[1][2]}</p><p>{pl_table_rows[2][2]}</p><p>{pl_table_rows[3][2]}</p><p>{pl_table_rows[4][2]}</p>
                        </div>
                        <div class="prem_leg_col4">
                            <b>W</b><p>{pl_table_rows[0][3]}</p><p>{pl_table_rows[1][3]}</p><p>{pl_table_rows[2][3]}</p><p>{pl_table_rows[3][3]}</p><p>{pl_table_rows[4][3]}</p>
                        </div>
                        <div class="prem_leg_col5">
                            <b>D</b><p>{pl_table_rows[0][4]}</p><p>{pl_table_rows[1][4]}</p><p>{pl_table_rows[2][4]}</p><p>{pl_table_rows[3][4]}</p><p>{pl_table_rows[4][4]}</p>
                        </div>
                        <div class="prem_leg_col6">
                            <b>L</b><p>{pl_table_rows[0][5]}</p><p>{pl_table_rows[1][5]}</p><p>{pl_table_rows[2][5]}</p><p>{pl_table_rows[3][5]}</p><p>{pl_table_rows[4][5]}</p>
                        </div>
                    </div>
                </div>

                <div class="mlb">
                    <h3>NL East Standings</h3>
                    <div class="mlb_grid">
                        <div class="mlb_col1">
                            <i>.</i><p>{mlb_table_rows[0][0]}</p><p>{mlb_table_rows[1][0]}</p><p>{mlb_table_rows[2][0]}</p><p>{mlb_table_rows[3][0]}</p><p>{mlb_table_rows[4][0]}</p>
                        </div>
                        <div class="mlb_col2">
                            <b>W</b><p>{mlb_table_rows[0][1]}</p><p>{mlb_table_rows[1][1]}</p><p>{mlb_table_rows[2][1]}</p><p>{mlb_table_rows[3][1]}</p><p>{mlb_table_rows[4][1]}</p>
                        </div>
                        <div class="mlb_col3">
                            <b>L</b><p>{mlb_table_rows[0][2]}</p><p>{mlb_table_rows[1][2]}</p><p>{mlb_table_rows[2][2]}</p><p>{mlb_table_rows[3][2]}</p><p>{mlb_table_rows[4][2]}</p>
                        </div>
                        <div class="mlb_col4">
                            <b>rdif</b><p>{mlb_table_rows[0][3]}</p><p>{mlb_table_rows[1][3]}</p><p>{mlb_table_rows[2][3]}</p><p>{mlb_table_rows[3][3]}</p><p>{mlb_table_rows[4][3]}</p>
                        </div>
                        <div class="mlb_col5">
                            <b>pyw</b><p>{mlb_table_rows[0][4]}</p><p>{mlb_table_rows[1][4]}</p><p>{mlb_table_rows[2][4]}</p><p>{mlb_table_rows[3][4]}</p><p>{mlb_table_rows[4][4]}</p>
                        </div>
                        <div class="mlb_col6">
                            <b>l20</b><p>{mlb_table_rows[0][5]}</p><p>{mlb_table_rows[1][5]}</p><p>{mlb_table_rows[2][5]}</p><p>{mlb_table_rows[3][5]}</p><p>{mlb_table_rows[4][5]}</p>
                        </div>
                    </div>
                </div>

                <div class="b1g">
                    <h3>B1G NCAAM Standings</h3>
                    <div class="b1g_grid">
                        <div class="b1g_col1">
                            <i>.</i><p>{ncaam_table_rows[0][0]}</p><p>{ncaam_table_rows[1][0]}</p><p>{ncaam_table_rows[2][0]}</p><p>{ncaam_table_rows[3][0]}</p><p>{ncaam_table_rows[4][0]}</p>
                        </div>
                        <div class="b1g_col2">
                            <b>W</b><p>{ncaam_table_rows[0][1]}</p><p>{ncaam_table_rows[1][1]}</p><p>{ncaam_table_rows[2][1]}</p><p>{ncaam_table_rows[3][1]}</p><p>{ncaam_table_rows[4][1]}</p>
                        </div>
                        <div class="b1g_col3">
                            <b>L</b><p>{ncaam_table_rows[0][2]}</p><p>{ncaam_table_rows[1][2]}</p><p>{ncaam_table_rows[2][2]}</p><p>{ncaam_table_rows[3][2]}</p><p>{ncaam_table_rows[4][2]}</p>
                        </div>
                        <div class="b1g_col4">
                            <b>PCT</b><p>{ncaam_table_rows[0][3]}</p><p>{ncaam_table_rows[1][3]}</p><p>{ncaam_table_rows[2][3]}</p><p>{ncaam_table_rows[3][3]}</p><p>{ncaam_table_rows[4][3]}</p>
                        </div>
                        <div class="b1g_col5">
                            <b>tPG</b><p>{ncaam_table_rows[0][4]}</p><p>{ncaam_table_rows[1][4]}</p><p>{ncaam_table_rows[2][4]}</p><p>{ncaam_table_rows[3][4]}</p><p>{ncaam_table_rows[4][4]}</p>
                        </div>
                        <div class="b1g_col6">
                            <b>oPG</b><p>{ncaam_table_rows[0][5]}</p><p>{ncaam_table_rows[1][5]}</p><p>{ncaam_table_rows[2][5]}</p><p>{ncaam_table_rows[3][5]}</p><p>{ncaam_table_rows[4][5]}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="main_body">
                <div class="main_center_story">
                    <h1>{final_fangraphs_list[0]}</h1>
                    <h4><i>Fangraphs Community</i></h4>
                    <p>{final_fangraphs_list[1]}</p>
                </div>
                <div class="main_right_story">
                    <h1>{nasa_list[0]}</h1>
                    <h4><i>NASA Blogs</i></h4>
                    <p>{nasa_list[1]}</p>
                </div>
                <div class="main_left_story">
                    <h1>{final_history_list[0]}</h1>
                    <h4><i>History Channel</i></h4>
                    <p>{final_history_list[1]}</p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""


# WRITING NEWSPAPER
with open('../reuben/newspaper.html', 'w') as newspaper_brief:
    newspaper_brief.write(html_script)


# OPENING NEWSPAPER
webbrowser.open_new_tab('file:///Users/lucasnelson/Desktop/MorningRoutine/reuben/newspaper.html')
