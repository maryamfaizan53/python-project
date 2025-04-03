def greet(name:str,message: str):
    print(f"Hello {name}, {message}")
    
def main():
    name = input("Enter your name: ")
    message = input("Enter a message: ")
    greet(name,message) 
if __name__ == "__main__":
    main()         