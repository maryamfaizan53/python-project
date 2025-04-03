import random

def main():
    guessed_num = random.randint(1, 99)  # Random number to guess
    user_input = int(input("Guess a number between 1 - 99: "))  # User's first guess

    while guessed_num != user_input:
        if user_input > guessed_num:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        
        # Get a new guess from the user
        user_input = int(input("Enter a new guess: "))

    print(f"Congrats! The number was {guessed_num}")

if __name__ == "__main__":
    main()
