import random
num_of_rounds = 5
def main():
    print("Welcome to the Hi-Low game...")
    your_score = 0
    for i in range(num_of_rounds):
        print("Round",i + 1)
        num : int = random.randint(1, 100)
        your_num : int = random.randint(1,100)
        print("Your number is" , your_num)
        guessed_num = input("Do you think your number is higher or lower than the computer's?: ")
    
        higher_and_correct : bool = guessed_num == 'higher' and your_num > num
        lower_and_correct : bool = guessed_num == 'lower' and your_num < num
    
        if higher_and_correct or lower_and_correct:
            print("You guessed correctly the computer number was!" , num)
            your_score += 1
        else:
            print("You guessed incorrectly the computer number was", num)
        
     # keep track of your score
        print("Your score is now" , your_score) 
        print() 
    print("Your final score is ", your_score)   
    if your_score == num_of_rounds:
        print("You won!")   
    elif your_score > num_of_rounds //2:
        print("Good job you did great")
    else:
        print("You lost! Better luck next time!")   
    
        
if __name__ == '__main__':
    main()       
    
    