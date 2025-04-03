import random
import time

# Native search function
def native_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# Binary search function
def binary_search(l, target, low, high):
    if low > high:
        return -1  # Base case: target not found
    
    midpoint = (low + high) // 2  # Calculate midpoint

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:  # Search in the left half
        return binary_search(l, target, low, midpoint - 1)
    else:  # Search in the right half
        return binary_search(l, target, midpoint + 1, high)

if __name__ == '__main__':  # Fixed __name__ condition
    length = 10000
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))

    sorted_list = sorted(list(sorted_list))  # Fix indentation

    target = random.choice(sorted_list)  # Pick a random target

    # Measure native search time
    start = time.time()
    native_search(sorted_list, target)
    end = time.time()
    print("Native search time:", (end - start) / length, "seconds")

    # Measure binary search time
    start = time.time()
    binary_search(sorted_list, target, 0, len(sorted_list) - 1)
    end = time.time()
    print("Binary search time:", (end - start) / length, "seconds")
