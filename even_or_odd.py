"Return 'Even' if number is even, 'Odd' otherwise."

# Best Practice
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"    

# Me
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
number = even_or_odd(5)
print(number)