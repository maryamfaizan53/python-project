def average(a,b):
   
    avg = (a + b) / 2
    return avg

def main():
    avg_1 = average(10, 20)
    avg_2 = average(20, 30)
    final = average (avg_1, avg_2)
    print("avg_1",avg_1)
    print("avg_2", avg_2)
    print("final", final)
if __name__ == "__main__":
    main()    

    
