station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

def navigate_research_station(station_layout, observations):
    station_layout_set = set(station_layout)
    count = 0
   # print(station_layout_set)
    for species in observations:
        if species in station_layout_set:
            count += 1
    return species, count
            



print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))