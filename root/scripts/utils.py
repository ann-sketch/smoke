# Changes 80.00% to 80 for computation
def prepare_values(data):
    for category_idx in data["games"]:
        for match in category_idx["matches"]:
            prob = match["prob"]
            for key in prob: prob[key] = prob[key].strip(".00%")
    return data