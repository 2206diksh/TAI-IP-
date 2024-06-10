def ask_question(question, choices, correct_choice):
    """
    Ask a single question to the user and return if they were correct.

    :param question: The question string
    :param choices: A list of possible answers
    :param correct_choice: The index (0-based) of the correct answer in choices
    :return: True if the user answered correctly, False otherwise
    """
    print(question)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")

    while True:
        try:
            user_answer = int(input("Enter the number of your choice: "))
            if 1 <= user_answer <= len(choices):
                return user_answer - 1 == correct_choice
            else:
                print("Invalid choice. Please select a number between 1 and", len(choices))
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    """
    Run the quiz for the user, asking each question in turn.

    :param questions: A list of tuples, each containing a question string, a list of choices, and the index of the correct choice
    :return: None
    """
    score = 0

    for question, choices, correct_choice in questions:
        if ask_question(question, choices, correct_choice):
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")

    print(f"Your final score is {score}/{len(questions)}.")

# Example questions
questions = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2),
    ("What is 2 + 2?", ["3", "4", "5", "6"], 1),
    ("Who wrote 'Hamlet'?", ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"], 2)
]

# Run the quiz
run_quiz(questions)
