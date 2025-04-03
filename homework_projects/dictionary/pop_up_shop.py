def main():
    fruits = {"apple": 40, "Banana": 20, "kiwi": 34, "Mango": 19, "Strawberry": 40}
    total_cost = 0
    
    for fruit_name, price in fruits.items():
        while True:
            try:
                quantity = int(input(f"How many {fruit_name} do you want to buy?: "))
                if quantity < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
        total_cost += price * quantity
        
    print(f"Your total is ${total_cost}")

if __name__ == "__main__":
    main()
