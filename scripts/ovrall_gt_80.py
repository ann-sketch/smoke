# Python3 script to get all odds greater than 80%

import json, os

def ovrall_gt_80(data):
    ovrall_gt_80 = []
    dest_dir = os.path.join(os.getcwd(), 'api/ovrall_gt_80.json')
    for category_idx in data["games"]:
        for match in category_idx["matches"]:
            match_date = match["match_date"]
            match_time = match["match_time"]
            match_status = match["match_status"]

            home = match["match_hometeam_name"]
            away = match["match_awayteam_name"]

            prob = match["prob"]
            prev_home_name = ""
            for key in prob: 
                if prob[key] not in ["", "-"]:
                    prob[key] = int(prob[key])
                    if prob[key] > 80:
                        if home == prev_home_name:
                            ovrall_gt_80[-1]['odd_type_to_prob'][key] = prob[key]
                        else:
                            ovrall_gt_80.append({
                            'match_date':match_date,
                            'match_time':match_time,
                            'match_status':match_status,
                            'home':home,
                            'away':away,
                            'odd_type_to_prob': {key:prob[key]}
                            })
                        prev_home_name = home
    
    ovrall_gt_80.sort(key=lambda x: x['match_time'])
    json.dump(ovrall_gt_80, open(dest_dir, "w"))