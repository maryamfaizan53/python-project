max_val : int = 10000
def main():
    current = 0 
    next = 1
    while current < max_val:
        print(current)
        current, next = next, current + next
        
if __name__ == "__main__":
    main()        