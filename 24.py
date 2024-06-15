# QUESTION 24
def calculator():
    print("Simple Calculator")
    print("Enter 'quit' to exit")

    while True:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            print("Result:", a + b)
        elif operator == '-':
            print("Result:", a - b)
        elif operator == '*':
            print("Result:", a * b)
        elif operator == '/':
            if b == 0:
                print("Error: Cannot divide by zero")
            else:
                print("Result:", a / b)
        else:
            print("Invalid operator")

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            print("Exiting...")
            break
calculator()        