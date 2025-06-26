endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"


def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    count = 0

    for species in observed_species:
        if species in endangered_set:
            count += 1
    return species, count
         

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))