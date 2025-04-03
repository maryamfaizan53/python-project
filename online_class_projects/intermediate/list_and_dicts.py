def main():
    fruit_list: list = ["Apple", "Mango", "Banana", "Orange", "Cherry"]
    print(len(fruit_list))
    fruit_list.append('Grapes')
    print(len(fruit_list))
    print(fruit_list)

if __name__ == '__main__':
    main()  

def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def sliced_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Index out of range."

def index_game():
    lst = [1, 2, 3, 4, 5]
    print("Current List:", lst)
    operation = input("Choose an operation: access, modify, slice: ").strip().lower()
    
    if operation == 'access':
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == 'modify':
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new element: ") 
        print(modify_element(lst, index, new_value))   
    elif operation == 'slice':
        start = int(input("Enter start index: ")) 
        end = int(input("Enter end index: "))
        print(sliced_list(lst, start, end))
    else:
        print("Invalid operation.")

index_game()
