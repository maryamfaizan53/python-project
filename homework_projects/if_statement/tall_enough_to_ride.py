min_height = 4 

def main():

    user_height = float(input("Enter your height in foot: "))
    
    if user_height  >= min_height:
        print("You are elegible for ride.")
    else:
        print("You are not eligible for ride")
        
if __name__ == "__main__" :
    main()           