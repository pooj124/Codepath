venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = venue1_schedule.items() & venue2_schedule.items()
    return conflicts

#conflict = {}
#for key in venue1_schedule:
  # if key in venue1_schedule and venue1_schedule[key] == venue2_schedule[key]
        #conflicts[key] = venue1_schedule[key]
 #       return conflicts
    #else:
    # print(f"No match for key: {key}")


print(identify_conflicts(venue1_schedule, venue2_schedule))