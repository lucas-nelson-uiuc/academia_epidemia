from datetime import datetime
from bs4 import BeautifulSoup
import requests
import re


class InvalidTeamEntry(Exception):
    pass

class DataFormatter:

    def format_date(temp):
        return datetime.strptime(temp, '%Y-%m-%d').strftime('%A, %b %d, %Y')

    def format_time(temp):
        try:
            return '{}:{}'.format(int(temp[:temp.find(':')])-6, temp[temp.find(':')+1:])
        except:
            return 'TBD'

    def format_homeaway(venue, opposition, current):
        return (current, opposition) if venue == 'Home' else (opposition, current)

class TeamSchedule:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.bs = self.gather_beautiful_soup()
        self.team_data = self.gather_team_data()

    def gather_beautiful_soup(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup.find(id='matchlogs_for').find('tbody')

    def gather_team_data(self):
        team_data = []
        
        # what matches are on the team's schedule?
        for elem in self.bs:
            team_matchdata = []
            for data in re.split('</[a-zA-Z]+>', str(elem)):
                if ('data-stat="date"' in data) or ('data-stat="time"' in data) \
                                                or ('data-stat="comp"' in data) \
                                                or ('data-stat="round"' in data) \
                                                or ('data-stat="venue"' in data) \
                                                or ('data-stat="opponent"' in data):
                    team_matchdata.append(data[data.rfind('>') + 1 : ])
            team_data.append(team_matchdata)

        # which matches have they not played yet (including today)?
        return [l for l in team_data if (len(l) != 0) and \
            (datetime.today().date() <= datetime.strptime(l[0], '%Y-%m-%d').date())]

    def format_team_data(self):
        # how can I make the data look prettier?
        for match in self.team_data:
            match[1] = DataFormatter.format_time(match[1])
            match[-2], match[-1] = DataFormatter.format_homeaway(match[-2], match[-1], self.name)
        
        team_dict = {}
        
        # how can I gather competitions on a group (competition-stage) basis?
        for match in self.team_data:
            if match[0] not in team_dict:
                team_dict[match[0]] = {}
            if match[2] not in team_dict[match[0]]:
                team_dict[match[0]][match[2]] = {}
            if match[3] not in team_dict[match[0]][match[2]]:
                team_dict[match[0]][match[2]][match[3]] = [match[1], match[4], match[5]]

        return team_dict

class PremierLeagueSchedule:

    def __init__(self, team):
        self.team = team
        self.team_url = {
            'Arsenal': 'https://fbref.com/en/squads/18bb7c10/Arsenal-Stats',
            'Aston Villa': 'https://fbref.com/en/squads/8602292d/Aston-Villa-Stats',
            'Brentford': 'https://fbref.com/en/squads/cd051869/Brentford-Stats',
            'Brighton': 'https://fbref.com/en/squads/d07537b9/Brighton-and-Hove-Albion-Stats',
            'Burnley': 'https://fbref.com/en/squads/943e8050/Burnley-Stats',
            'Chelsea': 'https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats',
            'Crystal Palace': 'https://fbref.com/en/squads/47c64c55/Crystal-Palace-Stats',
            'Everton': 'https://fbref.com/en/squads/d3fd31cc/Everton-Stats',
            'Leeds United': 'https://fbref.com/en/squads/5bfb9659/Leeds-United-Stats',
            'Leicester City': 'https://fbref.com/en/squads/a2d435b3/Leicester-City-Stats',
            'Liverpool': 'https://fbref.com/en/squads/822bd0ba/Liverpool-Stats',
            'Manchester City': 'https://fbref.com/en/squads/b8fd03ef/Manchester-City-Stats',
            'Manchester Utd': 'https://fbref.com/en/squads/19538871/Manchester-United-Stats',
            'Newcastle Utd': 'https://fbref.com/en/squads/b2b47a98/Newcastle-United-Stats',
            'Norwich City': 'https://fbref.com/en/squads/1c781004/Norwich-City-Stats',
            'Southampton': 'https://fbref.com/en/squads/33c895d4/Southampton-Stats',
            'Tottenham': 'https://fbref.com/en/squads/361ca564/Tottenham-Hotspur-Stats',
            'Watford': 'https://fbref.com/en/squads/2abfe087/Watford-Stats',
            'West Ham': 'https://fbref.com/en/squads/7c21e445/West-Ham-United-Stats',
            'Wolves': 'https://fbref.com/en/squads/8cec06e1/Wolverhampton-Wanderers-Stats'
        }
        self.team_color = {
            'Arsenal': '1;37;41',
            'Aston Villa': '1;31;45',
            'Brentford': '1;33;41',
            'Brighton': '0;37;44',
            'Burnley': '0;34;31',
            'Chelsea': '6;30;44',
            'Crystal Palace': '1;35;41',
            'Everton': '1;34;47',
            'Leeds United': '1;33;47',
            'Leicester City': '0;37;45',
            'Liverpool': '1;31;47',
            'Manchester City': '1;37;44',
            'Manchester Utd': '1;37;41',
            'Newcastle Utd': '1;37;40',
            'Norwich City': '1;33;42',
            'Southampton': '1;31;40',
            'Tottenham': '0;37;45',
            'Watford': '1;33;40',
            'West Ham': '1;34;41',
            'Wolves': '1;37;43'
        }

    def verify_teams_url(self):
        # are all the team(s) I entered in the Premier League?
        if self.team == 'All':
            self.team = ','.join(list(self.team_url.keys()))
        try:
            for team in self.team.split(','):
                if team.strip() not in self.team_url.keys():
                    raise InvalidTeamEntry
            print(f"> Successfully entered {len(self.team.split(','))} teams: {self.team}"
                    if len(self.team.split(',')) > 1
                    else f"> Successfully entered {len(self.team.split(','))} team: {self.team}")
        except InvalidTeamEntry:
            print(f'!! WARNING !! {team.strip()} not in Premier League')
        except:
            print('error')

    def gather_teams_schedule(self):
        master_dict = {}
        for team in self.team.split(','):
            tmsc = TeamSchedule(team.strip(), self.team_url[team.strip()])
            data = tmsc.format_team_data()
            for date in data:
                # are teams playing on a different date?
                if date not in master_dict:
                    master_dict[date] = {}
                for comp in data[date]:
                    # are teams playing in a different competition?
                    if comp not in master_dict[date]:
                        master_dict[date][comp] = {}
                    for matchweek in data[date][comp]:
                        # are teams playing in a different round?
                        if matchweek not in master_dict[date][comp]:
                            master_dict[date][comp][matchweek] = []
                        master_dict[date][comp][matchweek].append(data[date][comp][matchweek])
        return master_dict

    def output_teams_schedule(self):
        master = dict(sorted(self.gather_teams_schedule().items()))
        retr_str = ''
        for date in master:
            retr_str += '{:=^55}==\n'.format(' ' + DataFormatter.format_date(date) + ' ')
            for comp in master[date]:
                retr_str += f'  || {comp} ||\n'
                for round in master[date][comp]:
                    retr_str += f'    >> {round} <<\n'
                    for game in master[date][comp][round]:
                        try:
                            color_home = f'\x1b[{self.team_color[game[1]]}m{game[1]}\x1b[0m'
                        except:
                            color_home = f'\x1b[1;37;40m{game[1]}\x1b[0m'
                        try:
                            color_away = f'\x1b[{self.team_color[game[2]]}m{game[2]}\x1b[0m'
                        except:
                            color_away = f'\x1b[0;30;47m{game[2]}\x1b[0m'
                        if f'         ({game[0]}) {color_away} at {color_home}\n' in retr_str:
                            continue
                        retr_str += f'         ({game[0]}) {color_away} at {color_home}\n'
            retr_str += '\n'

        print(retr_str)

if __name__ == '__main__':
    query_team = input('> Enter team name ("all" for all teams): ').title()
    prem = PremierLeagueSchedule(query_team)
    prem.verify_teams_url()
    prem.output_teams_schedule()
