import requests

response=requests.get("https://thesportsdb.com/api/v1/json/3/all_leagues.php")
all_leagues=response.json()

response=requests.get("https://thesportsdb.com/api/v1/json/3/search_all_teams.php?l=NBA")
all_teams_NBA=response.json()


for team in all_teams_NBA['teams']:
    print(team['strTeam'])