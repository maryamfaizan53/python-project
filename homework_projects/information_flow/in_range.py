def in_range(n: int, lower: int, upper: int):
    if n >= lower and n <= upper:
        return True
    else:
        return False

def main():
    user_input = int(input("Enter a number: "))
    lower = int(input("Enter a lower bound: "))
    upper = int(input("Enter an upper bound: "))

    if in_range(user_input, lower, upper):
        print(f"{user_input} is between {lower} and {upper}")    
    else:
        print(f"{user_input} is NOT between {lower} and {upper}")  # Added else block

if __name__ == "__main__":
    main()
