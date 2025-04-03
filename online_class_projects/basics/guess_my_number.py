import random

def main():
    
    guess = random.randint(1,99)
    user_input = int(input("Guess a number: "))
    
    while guess != user_input:
    
        if user_input > guess:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
  
        print()
        user_input = int(input("Enter a new guess.")) 
    print("Congratz your guess is right.")
      
if __name__ == '__main__':
    main()           
    
    