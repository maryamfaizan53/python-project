PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48
def main():
    print("Here is the voting age analyzotion machine:")
    user_age : int = int(input("Enter your age if you are eligible or not for voting: "))
    if user_age >= PETURKSBOUIPO_AGE:
        print (f"You are eligible for voting in PETURKSBOUIPO where the voting age is " + str(PETURKSBOUIPO_AGE)+".") 
    else:    
        print (f"You are not eligible for voting in PETURKSBOUIPO where the voting age is " + str(PETURKSBOUIPO_AGE)+".") 
    if user_age >=STANLAU_AGE:
        print("You are eligible for voting in STANLAU where the voting age is " + str(STANLAU_AGE)+".")
    else:
        print("You are not eligible for voting in STANLAU where the voting age is " + str(STANLAU_AGE)+".")    
    if user_age >= MAYENGUA_AGE:
          print("You are eligible for voting in MAYENGUA where the voting age is " + str(MAYENGUA_AGE)+".")
    else:
        print("You are eligible for voting in MAYENGUA where the voting age is " + str(MAYENGUA_AGE)+".")

if __name__ == "__main__":
    main()    
    