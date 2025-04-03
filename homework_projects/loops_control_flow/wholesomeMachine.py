AFFIRMATION: str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION}")
    user_feedback = input()

    while user_feedback != AFFIRMATION:
        print("Please try again.")
        user_feedback = input()

    print("Thank you for your feedback.")

if __name__ == "__main__":
    main()
