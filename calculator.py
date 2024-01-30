def simple_calculator():
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        operator_choice = input("Enter the operator (+, -, *, /): ")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return

    if operator_choice == '+':
        result = x + y
    elif operator_choice == '-':
        result = x - y
    elif operator_choice == '*':
        result = x * y
    elif operator_choice == '/':
        if num2 != 0:
            result = x / y
        else:
            print("Error: Division by zero.")
            return
    else:
        print("Error: Invalid operator. Please enter +, -, *, or /.")
        return

    print(f"\nResult: {x} {operator_choice} {y} = {result}")

if __name__ == "__main__":
    simple_calculator()
