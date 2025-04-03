def count_even():
    user_input = int(input("Enter a number to find even numbers up to it: "))
    lst = []
    for i in range(1, user_input + 1):  # Corrected range syntax
        if i % 2 == 0:
            lst.append(i)
    return lst  # Moved return outside the loop

print(count_even())
  