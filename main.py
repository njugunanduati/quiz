import time
from datetime import datetime, timedelta
from database.config import Config
from database import check_user, save_score, save_user, get_questions


def get_user_answer():
    try:
        user_answer = input("Enter your answer: ").upper()
        accepted = ['A', 'B', 'C', 'D']
        if user_answer not in accepted:
            raise ValueError("Error! Your answer must be A, B, C or D")
        return user_answer
    except ValueError as e:
        print(str(e))
        return get_user_answer()


def calculate_score(user_answer, question, scores):
    if user_answer == question["correct"]:
        print(f"Correct!")
        print(f"Explanation. {question['explanation']}")
        scores.append(question["points"])
    else:
        print(f"Wrong! The correct answer is {question['options'][question['correct']]}")
        print(f"Explanation. {question['explanation']}")
        scores.append(0)


def start_quiz():
    print("\n Welcome to the Python Quiz Game!")
    print("-----------------------------------")
    print(
        "You will be asked multiple-choice questions. Answer by typing the letter corresponding to the correct answer."
    )
    first_name = input("Enter your first name: ").capitalize()
    last_name = input("Enter your last name: ").capitalize()
    email = input("Enter your email: ")
    # save the user details
    user_id = 0
    if not check_user(email):
        user_id = save_user(first_name, last_name, email)
        print(f"User {first_name} {last_name} has been registered successfully.")
        
    else:
        user_id = check_user(email)
        print(f"User {first_name} {last_name} already exists. Skipping registration.")
    print(f"Good luck! {first_name} {last_name} \n")
    print("\nLet's start the quiz!")
    questions = get_questions()
    scores = []
    total = sum([question['points'] for question in questions])
    # start the timer
    start_time = datetime.now()
    time_limit = timedelta(minutes=int(Config.QUIZ_DURATION))
    
    for question_number, question in enumerate(questions, start=1):
        current_time = datetime.now()
        elapsed_time = current_time - start_time
        if elapsed_time > time_limit:
            print(f"\nTime's up!")
            break
        print(f"{question_number}. {question['question']}")
        for option, option_text in question["options"].items():
            print(f"{option}. {option_text}")

        user_answer = get_user_answer()
        calculate_score(user_answer, question, scores)

        # show the time remaining
        remaining_time = time_limit - elapsed_time
        print(f"Time remaining: {remaining_time.seconds // 60} minutes and {remaining_time.seconds % 60} seconds")
        time.sleep(1)

    score = sum(scores)
    save_score(user_id, score, total)
    if total == 0:
        print("You did not answer any questions.")
    else:
        total_score = (score/total * 100)
        if total_score >= 50:
            print(f"Congratulations {first_name} {last_name}! You passed the quiz.")
        else:
            print(f"Sorry {first_name} {last_name}! You did not pass the quiz.")
        print(f"\nYour final score is: {int(total_score)}% out of {total}%")


if __name__ == "__main__":
    start_quiz()

