def get_last_element(lst):
    """Prints the last element of the provided list."""
    print(lst[len(lst) - 1])  # Alternative: print(lst[-1])

def get_lst():
    """Prompts the user to enter elements one by one and returns the final list."""
    lst = []
    elem = input("Please enter an element of the list or press Enter to stop: ")

    while elem != "":
        lst.append(elem)
        elem = input("Please enter another element or press Enter to stop: ")
    
    return lst

def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == "__main__":  # Corrected condition
    main()
