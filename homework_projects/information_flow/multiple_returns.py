def get_user_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    return first_name, last_name, email
def main():
    info = get_user_info()
    print(f"The given info of user is that {info}")
if __name__ == '__main__':
    main()    