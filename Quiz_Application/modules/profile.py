from modules.database import (
    load_users,
    save_users
)


# =========================================================
# SHOW PROFILE
# =========================================================

def show_profile(email):

    users = load_users()

    if email not in users:

        print("User not found.")
        return

    user = users[email]

    print("\n" + "=" * 45)
    print("                    PROFILE")
    print("=" * 45)

    print(
        f"Name       : {user['name']}"
    )

    print(
        f"Email      : {user['email']}"
    )

    print(
        f"Contact    : {user['contact']}"
    )

    print(
        f"Enrollment : {user['enroll']}"
    )

    print(
        f"College    : {user['college']}"
    )


# =========================================================
# UPDATE PROFILE
# =========================================================

def update_profile(email):

    users = load_users()

    if email not in users:

        print("User not found.")
        return

    user = users[email]

    print("\n" + "=" * 45)
    print("              UPDATE PROFILE")
    print("=" * 45)

    print("""
1. Update Name
2. Update Contact
3. Update College
4. Update Password
5. Back
""")

    choice = input(
        "Enter choice: "
    ).strip()

    if choice == "1":

        new_name = input(
            "Enter new name: "
        ).strip()

        if new_name:

            user["name"] = new_name

            print(
                "Name updated successfully."
            )

        else:

            print(
                "Name cannot be empty."
            )

    elif choice == "2":

        new_contact = input(
            "Enter new contact: "
        ).strip()

        if new_contact:

            user["contact"] = new_contact

            print(
                "Contact updated successfully."
            )

    elif choice == "3":

        new_college = input(
            "Enter new college: "
        ).strip()

        if new_college:

            user["college"] = new_college

            print(
                "College updated successfully."
            )

    elif choice == "4":

        new_password = input(
            "Enter new password: "
        ).strip()

        if new_password:

            user["password"] = new_password

            print(
                "Password updated successfully."
            )

        else:

            print(
                "Password cannot be empty."
            )

    elif choice == "5":

        return

    else:

        print(
            "Invalid choice."
        )

        return

    save_users(users)