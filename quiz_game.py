def start_quiz():
    print("\n Welcome to the Python Quiz Game!")
    print("-----------------------------------------")
    print(
        "You will be asked multiple-choice questions. Answer by typing the letter corresponding to the correct answer."
    )
    first_name = input("Enter your first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    print(f"Good luck! {first_name} {last_name} \n")
    scores = []
    total = 0
    questions = [
        {
            "question": "What is the output of print(2 * 3 ** 3)?",
            "options": {
                "A": "54",
                "B": "18",
                "C": "56",
                "D": "36"
            },
            "correct": "A",
            "explanation": "2 * 3 give an answer of 6. The ** represents power which is the same as 6^3 which comes to 54.",
            "points": 10
        },
        {
            "question": "Which of the following is a built-in data type in Python that represents a sequence of characters?",
            "options": {
                "A": "list",
                "B": "dictionary",
                "C": "tuple",
                "D": "set"
            },
            "correct": "C",
            "explanation": "A tuple is a sequence of elements enclosed in parentheses, separated by commas. It is a built-in data type in Python.",
            "points": 10
        },
        {
            "question": "What is the output of print(type('Hello World!'))?",
            "options": {
                "A": "str",
                "B": "int",
                "C": "float",
                "D": "boolean"
            },
            "correct": "A",
            "explanation": "The str() function converts any data type to a string.",
            "points": 10
        },
        {
            "question": "What is the output of print(10 % 3)?",
            "options": {
                "A": "0",
                "B": "1",
                "C": "2",
                "D": "3"
            },
            "correct": "B",
            "explanation": "The % operator returns the remainder of the division of the first operand by the second operand.",
            "points": 10
        },
        {
            "question": "What is the output of print(10 // 3)?",
            "options": {
                "A": "3",
                "B": "4",
                "C": "5",
                "D": "6"
            },
            "correct": "A",
            "explanation": "The // operator performs integer division of the first operand by the second operand, and the result is always an integer.",
            "points": 10
        },
        {
            "question": "Which of the following is a valid variable name in Python?",
            "options": {
                "A": "my_variable",
                "B": "my-variable",
                "C": "my variable",
                "D": "1my_variable"
            },
            "correct": "A",
            "explanation": "A valid variable name in Python can only contain alphanumeric characters and underscores, and it cannot start with a number.",
            "points": 10
        },
        {
            "question": "What is the output of print(True and False)?",
            "options": {
                "A": "True",
                "B": "False",
                "C": "1",
                "D": "0"
            },
            "correct": "B",
            "explanation": "The logical OR operator returns True if at least one of the operands is True.",
            "points": 10
        },
        {
            "question": "What is the output of print(True or False)?",
            "options": {
                "A": "True",
                "B": "False",
                "C": "1",
                "D": "0"
            },
            "correct": "A",
            "explanation": "The logical AND operator returns True only if both operands are True.",
            "points": 10
        },
        {
            "question": "What is enumerate used for in a for loop?",
            "options": {
                "A": "To iterate over a list",
                "B": "To iterate over a dictionary",
                "C": "To iterate over a range",
                "D": "To iterate over a string"
            },
            "correct": "A",
            "explanation": "Enumerate is a built-in function in Python that returns an enumerate object that produces a sequence of tuples containing a count (from start which defaults to 0) and the values obtained from iterating over an iterable.",
            "points": 10
        },
        {
            "question": "Which of the following is a built-in function in Python that returns the largest item in an iterable?",
            "options": {
                "A": "max()",
                "B": "min()",
                "C": "sum()",
                "D": "average()"
            },
            "correct": "A",
            "explanation": "max() returns the largest item in an iterable or the largest of two or more arguments.",
            "points": 10
        }
    ]

    for question_number, question in enumerate(questions, start=1):
        print(f"{question_number}. {question['question']}")
        for option, option_text in question["options"].items():
            print(f"{option}. {option_text}")

        user_answer = input("Enter your answer: ").upper()
        if user_answer == question["correct"]:
            print("Correct!")
            scores.append(question["points"])
        else:
            print(f"Wrong! The correct answer is {question['options'][question['correct']]}")
            print(f"{question['explanation']}")
            scores.append(0)
        total += question["points"]
    score = sum(scores)
    total_score = (score/total * 100)
    print('score', score)
    print('scores', scores)
    print(f"\nYour final score is: {int(total_score)}% out of {total}%")

start_quiz()
