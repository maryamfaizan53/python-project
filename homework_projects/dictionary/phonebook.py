def read_phn_nums():
    phonebook = {}  
    while True:
        name = input("Name: ").strip() 
        if name == "":
            break
        number = input("Number: ").strip()
        phonebook[name] = number  # Dictionary me store kar diya
    
    return phonebook  # LOOP ke baad return karna hai

def print_phonebook(phonebook):
    print("\n📖 Phonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")

def lookup_numbers(phonebook):        
    while True:
        name = input("\nFind name to look up: ").strip()
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number: {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")    

def main():
    phonebook = read_phn_nums()  # Numbers collect karna
    print_phonebook(phonebook)   # Phonebook print karna
    lookup_numbers(phonebook)    # Lookup function chalana

if __name__ == "__main__":
    main()
