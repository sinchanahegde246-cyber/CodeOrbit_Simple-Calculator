"""Simple Calculator with input validation and division-by-zero handling."""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("===== SIMPLE CALCULATOR =====")
    print("1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)")
    choice = input("Choose an operation (1-4): ").strip()
    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice. Please choose 1-4.")
        return
    first = get_number("Enter the first number: ")
    second = get_number("Enter the second number: ")
    try:
        if choice == "1":
            result, symbol = first + second, "+"
        elif choice == "2":
            result, symbol = first - second, "-"
        elif choice == "3":
            result, symbol = first * second, "*"
        else:
            if second == 0:
                raise ZeroDivisionError("You cannot divide by zero.")
            result, symbol = first / second, "/"
        print(f"Result: {first:g} {symbol} {second:g} = {result:g}")
    except ZeroDivisionError as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
