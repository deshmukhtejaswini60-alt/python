# password_generator.py - Simple Python Password Generator
# Generates random passwords with user-chosen length and complexity.

import random
import string


# ── Character Sets ─────────────────────────────────────────────────────────────

LOWERCASE  = string.ascii_lowercase          # a-z
UPPERCASE  = string.ascii_uppercase          # A-Z
DIGITS     = string.digits                   # 0-9
SPECIAL    = "!@#$%^&*"                      # special characters


# ── Generator Function ─────────────────────────────────────────────────────────

def generate_password(length, use_digits=True, use_special=True):
    """
    Generate a random password of the given length.

    Parameters:
        length      (int)  : Number of characters in the password.
        use_digits  (bool) : Include numbers (0-9).
        use_special (bool) : Include special characters (!@#$%^&*).

    Returns:
        str: The generated password.
    """
    # Build the pool of allowed characters based on complexity choice
    pool = LOWERCASE + UPPERCASE
    if use_digits:
        pool += DIGITS
    if use_special:
        pool += SPECIAL

    # Guarantee at least one character from each chosen category
    # so the password is never missing a required character type.
    required = [
        random.choice(LOWERCASE),
        random.choice(UPPERCASE),
    ]
    if use_digits:
        required.append(random.choice(DIGITS))
    if use_special:
        required.append(random.choice(SPECIAL))

    # Fill the rest of the password randomly from the full pool
    remaining = [random.choice(pool) for _ in range(length - len(required))]

    # Combine and shuffle so required characters aren't always at the start
    password_chars = required + remaining
    random.shuffle(password_chars)

    return "".join(password_chars)


# ── Helper: Get a Valid Length ─────────────────────────────────────────────────

def get_length():
    """
    Ask the user for a password length.
    Keeps asking until a positive integer (at least 4) is entered.
    Returns an int.
    """
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("  Length must be at least 4. Please try again.")
            else:
                return length
        except ValueError:
            print("  Please enter a whole number.")


# ── Helper: Get Complexity Choice ─────────────────────────────────────────────

def get_complexity():
    """
    Ask the user to pick a complexity level.
    Returns (use_digits, use_special) as a tuple of booleans.

    Levels:
      1 - Letters only         (a-z, A-Z)
      2 - Letters + Numbers    (a-z, A-Z, 0-9)
      3 - All characters       (a-z, A-Z, 0-9, !@#$%^&*)
    """
    print()
    print("  Complexity levels:")
    print("    1 - Letters only          (a-z, A-Z)")
    print("    2 - Letters + Numbers     (a-z, A-Z, 0-9)")
    print("    3 - All characters        (a-z, A-Z, 0-9, !@#$%^&*)")

    while True:
        choice = input("  Choose complexity (1 / 2 / 3): ").strip()
        if choice == "1":
            return False, False   # no digits, no special
        elif choice == "2":
            return True, False    # digits yes, special no
        elif choice == "3":
            return True, True     # digits yes, special yes
        else:
            print("  Please enter 1, 2, or 3.")


# ── Main Loop ──────────────────────────────────────────────────────────────────

def main():
    print("=" * 45)
    print("        Python Password Generator")
    print("=" * 45)

    while True:
        print()

        # Step 1: Get password length
        length = get_length()

        # Step 2: Get complexity level
        use_digits, use_special = get_complexity()

        # Step 3: Ask how many passwords to generate
        print()
        while True:
            try:
                count = int(input("How many passwords to generate? (1-10): "))
                if 1 <= count <= 10:
                    break
                print("  Please enter a number between 1 and 10.")
            except ValueError:
                print("  Please enter a whole number.")

        # Step 4: Generate and display the passwords
        print()
        print(f"  {'Generated Password' if count == 1 else 'Generated Passwords'}:")
        print("  " + "-" * 41)
        for i in range(count):
            pwd = generate_password(length, use_digits, use_special)
            label = f"  {i + 1}." if count > 1 else "  "
            print(f"{label:5} {pwd}")
        print("  " + "-" * 41)

        # Step 5: Ask to continue
        print()
        again = input("Generate more passwords? (yes/no): ").strip().lower()
        if again not in {"yes", "y"}:
            print("\nGoodbye!")
            break


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
