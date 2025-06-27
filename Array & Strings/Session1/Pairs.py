# Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. 
# Write a function can_pair() that accepts 

def can_pair(item_quantities):
    for quantity in item_quantities:
        if quantity % 2 != 0:
            return False
    return True
    
item_quantities = [2, 4, 6, 8]
print(can_pair(item_quantities))