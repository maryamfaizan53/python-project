def main():
    user_input = int(input("Enter a number to be doubled: "))  # Fixed input
    num = user_input * 2
    print(f"The double of {user_input} is {num}")  # Moved print before return
    return num

if __name__ == "__main__":
    main()  # Calling the function
