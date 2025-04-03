def main():
    
    joke = "Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
    print("Here is your joke bot")
    user_input : str = input("Tell me what you want a joke?: ").lower()
    if user_input == "joke":
        print(joke)
    else:
        print("I dont have any other info") 
if __name__ == '__main__':
    main()