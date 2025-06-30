# TandeTandemloop-FSD-

# Python Programming Language


# Problem 1: Simple Calculator using Class

# Define a Calculator class
class Calculator:
    def __init__(self, a, b, operation):
        # Initialize with two numbers and the operation type
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        # Perform calculation based on the operation
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "sub":
            return self.a - self.b
        elif self.operation == "mul":
            return self.a * self.b
        elif self.operation == "div":
            # Check for division by zero
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# User input section
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add, sub, mul, div): ").lower()

# Create object and call method
calc = Calculator(a, b, operation)
result = calc.calculate()

# Output result
print("Result:", result)



# Problem 2: Print first 'a' odd numbers starting from 1

# Take input from user
a = int(input("Enter a number: "))

# Loop 'a' times and print odd numbers using formula: 2*i + 1
for i in range(a):
    print(2*i + 1, end=", ")



# Problem 3: Print odd numbers
# If 'a' is odd, print 'a' odd numbers
# If 'a' is even, print 'a-1' odd numbers

# Take input
a = int(input("Enter a number: "))

# If even, reduce by 1
if a % 2 == 0:
    a -= 1

# Print odd numbers
for i in range(a):
    print(2*i + 1, end=", ")



# Problem 4: Count how many numbers in the list are divisible by 1 through 9

# Input list
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Dictionary to store result
result = {}

# Check divisibility for numbers 1 to 9
for i in range(1, 10):
    count = 0
    for num in input_list:
        if num % i == 0:
            count += 1
    result[i] = count

# Print the result dictionary
print(result)


