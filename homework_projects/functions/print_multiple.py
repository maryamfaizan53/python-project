def print_multiple(message:str,repeats:int):
    for i in range(repeats):
        print(message)
        
def main():
    message = input("Enter a message: ")  
    repaets = int(input("Enter the number of repeats: "))   
    print_multiple(message,repaets)
if __name__ == '__main__':
    main()                   