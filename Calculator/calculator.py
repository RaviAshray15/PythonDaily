def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,    
}

def calculator():
    should_accumulate = True
    num1 = float(input("Whats your first number?: "))

    while should_accumulate:
        for i in operations:
            print(i)
        symbol = input("Pick an operation: ")

        num2 = float(input("Whats your second number?: "))

        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start over: ")

        if choice == 'y':
            num1 = answer

        elif choice == 'n':
            should_accumulate = False
            calculator()
            
calculator()