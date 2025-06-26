species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

def most_endangered(species_list):
    if not species_list:
        return None
    
    min_population = species_list[0].get("population")
    endangered_species = species_list[0].get("name")

    for species in species_list:
        population = species.get("population")
        if population < min_population:
            min_population = population
            endangered_species = species.get("name")
    return endangered_species


print(most_endangered(species_list))