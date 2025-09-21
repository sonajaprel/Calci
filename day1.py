def calculator():
    print("---- Simple Command Line Calculator ----")
    print("Operations: +, -, *, /")
    print("Type 'exit' to quit\n")

    while True:
        # take input
        user_input = input("Enter expression (e.g., 5 + 3): ")

        # check exit
        if user_input.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break

        try:
            # split into parts
            parts = user_input.split()
            if len(parts) != 3:
                print(" Invalid format. Use: number operator number (e.g., 5 * 2)")
                continue

            num1, operator, num2 = parts
            num1, num2 = float(num1), float(num2)

            # perform calculation
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Division by zero is not allowed!")
                    continue
                result = num1 / num2
            else:
                print("Unsupported operator. Use +, -, *, /")
                continue

            print(f"Result: {result}\n")

        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    calculator()
