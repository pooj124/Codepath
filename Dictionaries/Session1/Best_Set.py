from collections import Counter

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}


def best_set(votes):
    max_count = Counter(votes.values())
    #print(max_count)
    largest = 0
    artist = None
    for key, value in max_count.items():
        if largest < value:
            largest = value
            artist = key
            return artist, largest
        return False
        



    
print(best_set(votes1))
print(best_set(votes2))