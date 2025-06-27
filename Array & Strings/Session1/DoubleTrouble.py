# Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter 
# and 
# multiplies each element in the list by two. Return the doubled list.

def Doubled(hunny_jars):
    doubled_honey = []

    for i in hunny_jars:
        doubled_honey.append(i * 2)
    return doubled_honey

hunny_jars = [1, 2, 3]
print(Doubled(hunny_jars))