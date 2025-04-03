def get_user_nums():
    user_num = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            user_num.append(int(user_input))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return user_num

def count_nums(num_list):
    num_dict = {}
    for num in num_list:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def print_counts(num_dict):
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    user_nums = get_user_nums()
    num_dict = count_nums(user_nums)
    print_counts(num_dict)

if __name__ == "__main__":
    main()
