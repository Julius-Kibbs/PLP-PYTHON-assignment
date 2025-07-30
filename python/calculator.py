print("Please the first number:")
first_number = float(input())

print("Please the second number:")
second_number = float(input())

print("Please choose an operation: +, -, *, /")
operation = input()

if operation == "+":
    result = first_number + second_number

elif operation == "-":
    result = first_number - second_number

elif operation == "*":
    result = first_number * second_number

elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Cannot divide by zero"

print("The answer is:", result)
