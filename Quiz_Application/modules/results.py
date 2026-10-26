from modules.database import load_results


def show_results(email):

    results = load_results()

    print("\n" + "=" * 50)
    print("                MY RESULTS")
    print("=" * 50)

    user_results = []

    for result in results:

        if result["email"] == email:

            user_results.append(result)

    if not user_results:

        print(
            "\nYou have not attempted "
            "any quiz yet."
        )

        input(
            "\nPress ENTER to continue..."
        )

        return

    for index, result in enumerate(
        user_results,
        start=1
    ):

        print(
            f"\nAttempt {index}"
        )

        print("-" * 35)

        print(
            f"Subject    : "
            f"{result['subject']}"
        )

        print(
            f"Score      : "
            f"{result['score']}/"
            f"{result['total']}"
        )

        print(
            f"Percentage : "
            f"{result['percentage']:.2f}%"
        )

        if result["percentage"] >= 40:

            print(
                "Status     : PASS ✓"
            )

        else:

            print(
                "Status     : FAIL ✗"
            )

    print("\n" + "=" * 50)

    input(
        "Press ENTER to continue..."
    )