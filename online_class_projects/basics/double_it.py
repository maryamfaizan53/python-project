def main():
    
    num = int(input("Enter a number: "))
    
    while num < 100:
        print(num , end = " ")
        num  *= 2
    print(num)    
if __name__ == '__main__':
    main()    