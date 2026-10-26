import threading


def get_answer_with_timeout(timeout):

    answer = [None]

    def take_input():

        try:

            answer[0] = input(
                "\nYour answer: "
            )

        except EOFError:

            answer[0] = None

    input_thread = threading.Thread(
        target=take_input,
        daemon=True
    )

    input_thread.start()

    input_thread.join(timeout)

    if input_thread.is_alive():

        return None

    return answer[0]