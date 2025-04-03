def print_sentence(word, parts_of_speech):
    if parts_of_speech == 0:
        print("I have to add this " + word + "in my collection")
    elif parts_of_speech == 1:
        print("I am " + word)
    elif parts_of_speech == 2:
        print(f"You are so {word}") 
    else:
        print("Invalid word")
def main():
    word = input("Enter a noun , verb, or adjective : ")
    print("for noun = 0 , for verb = 1, for adjective = 2")
    parts_of_speech = int(input("Enter a number between 0 and 2 : "))
    print_sentence(word, parts_of_speech)
if __name__ == "__main__":
    main()    
            
                   
    