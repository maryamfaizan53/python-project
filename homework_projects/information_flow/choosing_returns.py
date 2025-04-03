age_check :int = 18 # us age
def is_age(age):
    if age >= age_check:
        return True
    else:
        return False
def main():
    age = int(input("How is your age?")) 
    print(is_age(age))
if __name__ == "__main__":
    main()       
    
    