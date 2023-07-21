class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Creating an object of MathOperations
math_obj = MathOperations()

# The add method with two arguments will be called
result1 = math_obj.add(2, 3)
print("Result 1:", result1)  # Output: 5

# The add method with three arguments will be called
result2 = math_obj.add(2, 3, 4)
print("Result 2:", result2)  # Output: 9
