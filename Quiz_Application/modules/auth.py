from modules.database import (
    load_users,
    save_users
)

from modules.profile import (
    show_profile,
    update_profile
)

from modules.quiz import attempt_quiz

from modules.results import show_results


# =========================================================
# REGISTRATION
# =========================================================

def registration():

    users = load_users()

    print("\n" + "=" * 45)
    print("                 REGISTRATION")
    print("=" * 45)

    name = input(
        "Enter Name: "
    ).strip()

    email = input(
        "Enter Email: "
    ).strip().lower()

    contact = input(
        "Enter Contact: "
    ).strip()

    enroll = input(
        "Enter Enrollment Number: "
    ).strip()

    college = input(
        "Enter College: "
    ).strip()

    password = input(
        "Enter Password: "
    ).strip()

    # Basic validation

    if not name:

        print("\nName cannot be empty.")
        return

    if not email:

        print("\nEmail cannot be empty.")
        return

    if not enroll:

        print("\nEnrollment number cannot be empty.")
        return

    if not password:

        print("\nPassword cannot be empty.")
        return

    # Duplicate email

    if email in users:

        print(
            "\nA user with this email "
            "already exists."
        )

        return

    # Duplicate enrollment

    for user in users.values():

        if user["enroll"] == enroll:

            print(
                "\nThis enrollment number "
                "is already registered."
            )

            return

    # Create user

    users[email] = {

        "name": name,

        "email": email,

        "contact": contact,

        "enroll": enroll,

        "college": college,

        "password": password
    }

    save_users(users)

    print(
        "\nRegistration successful!"
    )

    print(
        "You can now login from the main menu."
    )


# =========================================================
# LOGIN
# =========================================================

def login():

    users = load_users()

    print("\n" + "=" * 45)
    print("                    LOGIN")
    print("=" * 45)

    email = input(
        "Enter Email: "
    ).strip().lower()

    password = input(
        "Enter Password: "
    ).strip()

    if email not in users:

        print(
            "\nUser not found."
        )

        return

    if users[email]["password"] != password:

        print(
            "\nIncorrect password."
        )

        return

    print(
        "\nLogin successful!"
    )

    print(
        f"Welcome, {users[email]['name']}!"
    )

    user_menu(email)


# =========================================================
# USER DASHBOARD
# =========================================================

def user_menu(email):

    while True:

        print("\n" + "=" * 50)
        print("                 DASHBOARD")
        print("=" * 50)

        print("""
1. Profile
2. Update Profile
3. Attempt Quiz
4. Result
5. Logout
""")

        choice = input(
            "Enter choice: "
        ).strip()

        if choice == "1":

            show_profile(email)

        elif choice == "2":

            update_profile(email)

        elif choice == "3":

            attempt_quiz(email)

        elif choice == "4":

            show_results(email)

        elif choice == "5":

            print(
                "\nLogged out successfully!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )