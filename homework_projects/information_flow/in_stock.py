def main():
    answer = input("Enter a fruit: ").lower()  # Convert input to lowercase for consistency
    stock = is_available(answer)

    if stock:  # If stock has a valid value (non-zero)
        print(f"This fruit is available in stock with {stock} pieces.")
    else:
        print("This fruit is not in stock.")

def is_available(answer):
    fruit_stock = {
        "apple": 200,
        "orange": 28,
        "banana": 183
    }
    
    return fruit_stock.get(answer, 0)  # Return stock count if available, else return 0

if __name__ == '__main__':
    main()
