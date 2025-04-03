def get_first_element(list_num):
    """Prints the first element of a list if it is not empty."""
    if list_num:  # Check if list is not empty
        print("First element:", list_num[0])
    else:
        print("The list is empty!")

def get_list_from_user():
    """Takes input from the user and returns a list of entered elements."""
    list_num = []
    elem = input("Enter an element for the list (or press Enter to stop): ")
    
    while elem != "":  # Loop continues until user presses Enter
        list_num.append(elem)
        elem = input("Enter another element (or press Enter to stop): ")
    
    return list_num

def main():
    list_num = get_list_from_user()  # Correct function call
    get_first_element(list_num)  # Call function to print first element

if __name__ == "__main__":
    main()
