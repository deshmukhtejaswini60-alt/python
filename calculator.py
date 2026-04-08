# calculator.py - Simple Python Calculator
# A beginner-friendly calculator that supports +, -, *, /
# with input validation, division-by-zero handling, and a loop.


# ── Operation Functions ────────────────────────────────────────────────────────

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """
    Return the result of a divided by b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# ── Helper: Get a Number from the User ────────────────────────────────────────

def get_number(prompt):
    """
    Keep asking until the user enters a valid number.
    Returns a float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  That's not a valid number. Please try again.")


# ── Helper: Get an Operation from the User ────────────────────────────────────

def get_operation():
    """
    Keep asking until the user chooses a valid operation.
    Returns one of: '+', '-', '*', '/'
    """
    valid = {"+", "-", "*", "/"}
    while True:
        op = input("Choose an operation (+, -, *, /): ").strip()
        if op in valid:
            return op
        print(f"  '{op}' is not a valid operation. Please choose +, -, *, or /.")


# ── Main Calculator Loop ───────────────────────────────────────────────────────

def main():
    print("=" * 40)
    print("       Simple Python Calculator")
    print("=" * 40)

    while True:
        print()

        # Step 1: Get two numbers from the user
        num1 = get_number("Enter the first number:  ")
        num2 = get_number("Enter the second number: ")

        # Step 2: Get the desired operation
        op = get_operation()

        # Step 3: Perform the operation and show the result
        try:
            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)

            # Display result — show as int if it's a whole number
            display = int(result) if result == int(result) else result
            print(f"\n  Result: {num1} {op} {num2} = {display}")

        except ZeroDivisionError as e:
            print(f"\n  Error: {e}")

        # Step 4: Ask if the user wants another calculation
        print()
        again = input("Do another calculation? (yes/no): ").strip().lower()
        if again not in {"yes", "y"}:
            print("\nGoodbye!")
            break


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
