artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

def lineup(artists, set_times):
    matched = dict(zip(artists, set_times))
    return matched

print(lineup(artists1, set_times1))