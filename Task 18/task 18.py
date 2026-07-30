

import random


best_score = None

print("=" * 50)
print("      WELCOME TO THE GUESS THE NUMBER GAME")
print("=" * 50)

play_again = "yes"

while play_again.lower() == "yes":

    
    secret_number = random.randint(1, 100)

    
    guesses = []
    attempts = 0
    max_chances = 10
    guessed_correctly = False

    print("\nI have selected a number between 1 and 100.")
    print(f"You have {max_chances} chances to guess it.")

   
    while attempts < max_chances:

        guess = int(input("\nEnter your guess: "))

        guesses.append(guess)
        attempts += 1

        if guess > secret_number:
            print("Too High! Try Again.")

        elif guess < secret_number:
            print("Too Low! Try Again.")

        else:
            print("\nCongratulations! You guessed the correct number.")
            guessed_correctly = True
            break

        print(f"Remaining Chances: {max_chances - attempts}")

    
    if not guessed_correctly:
        print("\nGame Over!")
        print(f"The correct number was: {secret_number}")

    
    print("\n========== GAME SUMMARY ==========")
    print("Guessed Numbers :", guesses)

    if len(guesses) > 0:
        print("First Guess     :", guesses[0])
        print("Last Guess      :", guesses[-1])

    print("Total Guesses   :", len(guesses))
    print("Attempts Taken  :", attempts)

    
    if guessed_correctly:
        if best_score is None or attempts < best_score:
            best_score = attempts

    if best_score is not None:
        print("Best Score      :", best_score, "attempt(s)")
    else:
        print("Best Score      : No successful game yet.")

    print("=" * 35)

    
    play_again = input("\nDo you want to play again? (Yes/No): ").strip().lower()

print("\nThank you for playing the Guess the Number Game!")
print("Have a great day!")