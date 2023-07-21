"""
Declare "Senior" if age 55 or older and handicap above seven, otherwise
declare "Open". If the input is a list of bivariable lists [age, handicap],
return a string holding each new member's status. 
"""

# Best Practice
def openOrSenior(data):
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

# Me

def openOrSenior(data):
    output = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output

openOrSenior = openOrSenior([[55, 20], [19, 5], [23, 14], [62, 3], [37, -1]])
print(openOrSenior)