import json
import os


# =========================================================
# PATH CONFIGURATION
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(
    BASE_DIR,
    "data"
)

USERS_FILE = os.path.join(
    DATA_DIR,
    "users.json"
)

QUESTIONS_FILE = os.path.join(
    DATA_DIR,
    "questions.json"
)

RESULTS_FILE = os.path.join(
    DATA_DIR,
    "results.json"
)


# =========================================================
# INITIALIZE DATA DIRECTORY AND FILES
# =========================================================

def ensure_data_files():

    os.makedirs(
        DATA_DIR,
        exist_ok=True
    )

    if not os.path.exists(USERS_FILE):

        save_data(
            USERS_FILE,
            {}
        )

    if not os.path.exists(RESULTS_FILE):

        save_data(
            RESULTS_FILE,
            []
        )


# =========================================================
# GENERIC LOAD FUNCTION
# =========================================================

def load_data(filename, default):

    try:

        with open(
            filename,
            "r"
        ) as file:

            return json.load(file)

    except (
        FileNotFoundError,
        json.JSONDecodeError
    ):

        return default


# =========================================================
# GENERIC SAVE FUNCTION
# =========================================================

def save_data(filename, data):

    with open(
        filename,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# =========================================================
# USER DATA
# =========================================================

def load_users():

    ensure_data_files()

    return load_data(
        USERS_FILE,
        {}
    )


def save_users(users):

    ensure_data_files()

    save_data(
        USERS_FILE,
        users
    )


# =========================================================
# QUESTION DATA
# =========================================================

def load_questions():

    return load_data(
        QUESTIONS_FILE,
        {}
    )


# =========================================================
# RESULT DATA
# =========================================================

def load_results():

    ensure_data_files()

    return load_data(
        RESULTS_FILE,
        []
    )


def save_results(results):

    ensure_data_files()

    save_data(
        RESULTS_FILE,
        results
    )