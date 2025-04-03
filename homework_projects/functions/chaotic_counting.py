import random

DONE_LIKELIHOOD = 0.5

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        print(curr_num)

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False
            
def main():
    print("I am going to count untill 10 or unt:")
    chaotic_counting()
    print("I am done counting")   
if __name__ == "__main__":
    main() 
     