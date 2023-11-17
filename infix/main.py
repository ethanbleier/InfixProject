# Need a stack of adds, subtracts, and ints
# Should represent a tree that looks like Examples/e1.png

# Define lambda functions for different operations
add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

# Function to convert between bracketed forms
def convert(expression):
    # Split the expression into components
    components = expression.split()

    # Identify the operator and operands
		# TODO: Operations need to go here


# Test the conversion
expression1 = '(1 + 2) - (4 - 1)'
expression2 = '(5 + 10) / (1 + 2)'
expression3 = '(+ 1 2)'

result1 = convert(expression1)
result2 = convert(expression2)
result3 = convert(expression3)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")