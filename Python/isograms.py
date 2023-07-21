"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
"""

# Best Practice
def is_isogram(string):
    return len(string) == len(set(string.lower()))

# Me
def is_isogram(string):
    letters = []    
    for character in string:
        if character.lower() not in letters:
            letters.append(character.lower())
    if len(string) == len(letters):
        return True
    else:
        return False