from modules.auth import registration, login


def main():

    while True:

        print("\n" + "=" * 50)
        print("              WELCOME TO QUIZ")
        print("=" * 50)

        print("""
Choose an option:

1. Registration
2. Login
3. Exit
""")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            registration()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nThank you for using Quiz Application!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()