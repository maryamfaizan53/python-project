import random

def main():
    for _ in range(10):
        num = random.randint(1, 100)
        print(num, end=' ')
    print()

if __name__ == "__main__":
    main()