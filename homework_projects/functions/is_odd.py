def main():
   for i in range(10):
    if is_odd(i):
       print(f"{i} is odd")
    else:
        print(f"{i} is even")   
def is_odd(val):
    return val % 2 == 1       
         
if __name__ == "__main__":
    main()
          