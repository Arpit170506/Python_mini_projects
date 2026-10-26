import random

from modules.database import (
    load_questions,
    load_results,
    save_results
)

from utils.timer import (
    get_answer_with_timeout
)


# =========================================================
# QUIZ CONFIGURATION
# =========================================================

QUESTIONS_PER_QUIZ = 5

TIME_PER_QUESTION = 30


# =========================================================
# QUIZ SUBJECT MENU
# =========================================================

def attempt_quiz(email):

    while True:

        print("\n" + "=" * 50)
        print("                ATTEMPT QUIZ")
        print("=" * 50)

        print("""
1. DSA
2. DBMS
3. Python
4. System Design
5. Back
""")

        choice = input(
            "Choose subject: "
        ).strip()

        if choice == "1":

            start_quiz(
                email,
                "DSA"
            )

        elif choice == "2":

            start_quiz(
                email,
                "DBMS"
            )

        elif choice == "3":

            start_quiz(
                email,
                "Python"
            )

        elif choice == "4":

            start_quiz(
                email,
                "System Design"
            )

        elif choice == "5":

            return

        else:

            print(
                "\nInvalid choice."
            )


# =========================================================
# START QUIZ
# =========================================================

def start_quiz(email, subject):

    question_database = load_questions()

    if subject not in question_database:

        print(
            "\nQuestion bank not available "
            "for this subject."
        )

        return

    question_bank = question_database[subject]

    # Make sure enough questions exist

    if len(question_bank) < QUESTIONS_PER_QUIZ:

        print(
            f"\nNot enough questions "
            f"available for {subject}."
        )

        return

    # =====================================================
    # RANDOM QUESTION SELECTION
    # =====================================================

    selected_questions = random.sample(
        question_bank,
        QUESTIONS_PER_QUIZ
    )

    # =====================================================
    # RANDOMIZE OPTIONS
    # =====================================================

    quiz_questions = []

    for question in selected_questions:

        options = question["options"].copy()

        random.shuffle(options)

        quiz_questions.append({

            "question":
                question["question"],

            "options":
                options,

            "answer":
                question["answer"]
        })

    # =====================================================
    # QUIZ INTRO
    # =====================================================

    print("\n" + "=" * 50)
    print(
        f"              {subject.upper()} QUIZ"
    )
    print("=" * 50)

    print(
        f"\nNumber of Questions : "
        f"{QUESTIONS_PER_QUIZ}"
    )

    print(
        f"Time Per Question   : "
        f"{TIME_PER_QUESTION} seconds"
    )

    print(
        "\nQuestions and options "
        "will be randomized."
    )

    print(
        "\nOnce the timer expires, "
        "the question will be marked wrong."
    )

    input(
        "\nPress ENTER to start the quiz..."
    )

    # =====================================================
    # QUIZ
    # =====================================================

    score = 0

    for index, question in enumerate(
        quiz_questions,
        start=1
    ):

        print("\n" + "-" * 50)

        print(
            f"Question {index}/"
            f"{QUESTIONS_PER_QUIZ}"
        )

        print(
            f"Time Limit: "
            f"{TIME_PER_QUESTION} seconds"
        )

        print("-" * 50)

        print(
            f"\n{question['question']}\n"
        )

        # Display randomized options

        for number, option in enumerate(
            question["options"],
            start=1
        ):

            print(
                f"{number}. {option}"
            )

        # =================================================
        # TIMER
        # =================================================

        answer = get_answer_with_timeout(
            TIME_PER_QUESTION
        )

        # =================================================
        # TIMEOUT
        # =================================================

        if answer is None:

            print(
                "\n⏰ TIME UP!"
            )

            print(
                "Question marked wrong."
            )

            continue

        # =================================================
        # ANSWER VALIDATION
        # =================================================

        try:

            answer = int(answer)

            if (
                answer < 1
                or answer > len(
                    question["options"]
                )
            ):

                print(
                    "\nInvalid option."
                )

                continue

            selected_answer = (
                question["options"][
                    answer - 1
                ]
            )

            # =================================================
            # CHECK CORRECT ANSWER
            # =================================================

            if (
                selected_answer
                == question["answer"]
            ):

                print(
                    "\n✓ Correct!"
                )

                score += 1

            else:

                print(
                    "\n✗ Wrong!"
                )

                print(
                    f"Correct answer: "
                    f"{question['answer']}"
                )

        except ValueError:

            print(
                "\nInvalid input."
            )

            print(
                "Question marked wrong."
            )

    # =====================================================
    # CALCULATE SCORE
    # =====================================================

    total = QUESTIONS_PER_QUIZ

    percentage = (
        score / total
    ) * 100

    # =====================================================
    # SAVE RESULT
    # =====================================================

    results = load_results()

    result = {

        "email": email,

        "subject": subject,

        "score": score,

        "total": total,

        "percentage": percentage
    }

    results.append(result)

    save_results(results)

    # =====================================================
    # DISPLAY RESULT
    # =====================================================

    print("\n" + "=" * 50)
    print("              QUIZ COMPLETED")
    print("=" * 50)

    print(
        f"Subject    : {subject}"
    )

    print(
        f"Score      : "
        f"{score}/{total}"
    )

    print(
        f"Percentage : "
        f"{percentage:.2f}%"
    )

    if percentage >= 40:

        print(
            "Status     : PASS ✓"
        )

    else:

        print(
            "Status     : FAIL ✗"
        )

    print("=" * 50)

    input(
        "\nPress ENTER to continue..."
    )