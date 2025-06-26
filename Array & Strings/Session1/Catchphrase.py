# Write a function print_catchphrase() that accepts a string character as a parameter 
# and prints the catchphrase of the given character as outlined in the table below.
# If the given character does not match one of the characters included above, 
# print "Sorry! I don't know <character>'s catchphrase!"

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh bother!")
    elif character == "Tigger":
        print("TTFN: Ta-ta for now!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly! old bear")
    else:
        print(f"Sorry! I DONT KNOW {character}s catchphrase!")

character = "Poojitha"
print(print_catchphrase(character))