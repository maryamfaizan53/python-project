def print_divisors(num:int):
    print("Here are the divisors of", num)
    for i in range(num):
        currt_div = i + 1
        if num % currt_div == 0:
            print(currt_div)
     
def main():
        num = int(input("Enter a number: "))
        print_divisors(num)
  

if __name__ == '__main__':
    main()            