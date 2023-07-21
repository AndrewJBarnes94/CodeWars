"""
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

"""

# Best Practice
def find_needle(haystack): return 'found the needle at position %d' % haystack.index('needle')

# Me
def find_needle(haystack):
    count = 0
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {count}"
        else:
            count += 1

haystack = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

needle = find_needle(haystack)
print(needle)