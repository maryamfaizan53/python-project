def main():
    sec = 1
    min = 60 
    hour = 60 * min
    day = 24 * hour
    week = 7* day
    month = 30 * day
    year = 12 * month
    
    input_year = int(input("Enter a number of years to calculate seconds: "))
    sec = sec*year
    print (f'There are {sec} seconds in  {input_year} years')
    
if __name__ == "__main__":
    main()    
    