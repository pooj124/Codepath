ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

def total_sales(ticket_sales):
    total = sum(value for value in ticket_sales.values())
    return total
        
        #total = 0

        #for value in my_dict.values():
    #try:
      #  total += value
   # except TypeError:
     #   continue

print(total_sales(ticket_sales))