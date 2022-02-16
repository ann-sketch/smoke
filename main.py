import json
from requests import get

fvalue = get("https://www.sonic-sports.eu/clients/sonic/apps/sonicai3/appApi.php").json()

games = fvalue["games"]

league0 = games[0]

return_json = []

for category_idx in games:
    for match in category_idx["matches"]:
        match_date = match["match_date"]
        match_time = match["match_time"]
        match_status = match["match_status"]
        league_name = match["match_status"]

        home = match["match_hometeam_name"]
        away = match["match_awayteam_name"]

        prob = match["prob"]

        odd_1 = prob['odd_1'].replace('.00','')
        odd_x = prob['odd_x'].replace('.00','')
        odd_2 = prob['odd_2'].replace('.00','')

        odd_x1 = prob['odd_1x'].replace('.00','')
        odd_12 = prob['odd_12'].replace('.00','')
        odd_x2 = prob['odd_x2'].replace('.00','')

        over2 = prob['o+2.5'].replace('.00','')
        under2 = prob['u+2.5'].replace('.00','')

        if odd_1 != "-":
            return_json.append({
                'match_date':match_date,
                'match_time':match_time,
                'match_status':match_status,
                'home':home,
                'away':away,
                'odd_1': odd_1,
                'odd_x':odd_x, 
                'odd_2':odd_2,
                'odd_x1': odd_x1, 
                'odd_12':odd_12, 
                'odd_x2':odd_x2,
                'over2':over2, 
                'under2':under2
                })

return_json.sort(key=lambda x: x['match_time'])

json.dump(return_json, open("./root/index.json", "w"))
