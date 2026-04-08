# rock_paper_scissors.py - Rock, Paper, Scissors Game
# Play against the computer with score tracking across multiple rounds.

import random


# ── Game Logic ─────────────────────────────────────────────────────────────────

CHOICES = ["rock", "paper", "scissors"]

# Maps each choice to what it beats
BEATS = {
    "rock":     "scissors",
    "scissors": "paper",
    "paper":    "rock",
}


def get_computer_choice():
    """Randomly pick rock, paper, or scissors for the computer."""
    return random.choice(CHOICES)


def get_user_choice():
    """
    Ask the user to type their choice.
    Keeps asking until a valid option is entered.
    Accepts full words or first letters (r / p / s).
    Returns one of: 'rock', 'paper', 'scissors'.
    """
    shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}

    while True:
        raw = input("Your choice (rock / paper / scissors): ").strip().lower()

        if raw in CHOICES:
            return raw
        elif raw in shortcuts:
            return shortcuts[raw]
        else:
            print(f"  '{raw}' is not valid. Type rock, paper, scissors (or r/p/s).")


def determine_winner(user, computer):
    """
    Compare user and computer choices.

    Returns:
        'win'  - user wins
        'lose' - computer wins
        'tie'  - it's a draw
    """
    if user == computer:
        return "tie"
    elif BEATS[user] == computer:
        return "win"
    else:
        return "lose"


# ── Display Helpers ────────────────────────────────────────────────────────────

EMOJIS = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}

def show_round_result(user, computer, outcome):
    """Print both choices and the round result."""
    print(f"\n  You chose    : {EMOJIS[user]}  {user.capitalize()}")
    print(f"  Computer chose: {EMOJIS[computer]}  {computer.capitalize()}")
    print()

    if outcome == "tie":
        print("  It's a tie!")
    elif outcome == "win":
        print(f"  {user.capitalize()} beats {computer} — You win this round!")
    else:
        print(f"  {computer.capitalize()} beats {user} — Computer wins this round!")


def show_score(user_score, computer_score, ties):
    """Print the current score."""
    print(f"\n  Score  →  You: {user_score}  |  Computer: {computer_score}  |  Ties: {ties}")


def show_final_score(user_score, computer_score, ties):
    """Print the final score and overall winner."""
    total = user_score + computer_score + ties
    print()
    print("=" * 45)
    print("             FINAL SCORE")
    print("=" * 45)
    print(f"  Rounds played : {total}")
    print(f"  You           : {user_score}")
    print(f"  Computer      : {computer_score}")
    print(f"  Ties          : {ties}")
    print("-" * 45)

    if user_score > computer_score:
        print("  Overall winner: YOU! Well played!")
    elif computer_score > user_score:
        print("  Overall winner: Computer. Better luck next time!")
    else:
        print("  Overall result: It's a draw!")
    print("=" * 45)


# ── Main Game Loop ─────────────────────────────────────────────────────────────

def main():
    print("=" * 45)
    print("       Rock, Paper, Scissors!")
    print("=" * 45)
    print("  Type 'quit' at any time to stop.\n")

    user_score     = 0
    computer_score = 0
    ties           = 0
    round_num      = 0

    while True:
        round_num += 1
        print(f"\n--- Round {round_num} ---")

        # Get user choice (allow quitting)
        raw = input("Your choice (rock / paper / scissors): ").strip().lower()
        if raw in {"quit", "q", "exit"}:
            break

        # Validate shortcut or full word
        shortcuts = {"r": "rock", "p": "paper", "s": "scissors"}
        if raw in shortcuts:
            raw = shortcuts[raw]

        if raw not in CHOICES:
            print(f"  '{raw}' is not valid. Type rock, paper, scissors (or r/p/s).")
            round_num -= 1   # don't count the invalid round
            continue

        user     = raw
        computer = get_computer_choice()
        outcome  = determine_winner(user, computer)

        # Update scores
        if outcome == "win":
            user_score += 1
        elif outcome == "lose":
            computer_score += 1
        else:
            ties += 1

        # Show round result and running score
        show_round_result(user, computer, outcome)
        show_score(user_score, computer_score, ties)

        print()
        again = input("Play another round? (yes/no or press Enter): ").strip().lower()
        if again in {"no", "n", "quit", "q"}:
            break

    # Show final score only if at least one round was played
    if round_num > 0 and (user_score + computer_score + ties) > 0:
        show_final_score(user_score, computer_score, ties)
    else:
        print("\nNo rounds played. Goodbye!")


# ── Entry Point ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
