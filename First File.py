# Introduction to Python

import time



def main():
    # A quiz application
    # Create some questions
    questions = [
        ("What is the colour of the sun?", "yellow"),
        ("How many things are in a dozen?", "12"),
        ("How many things are in a baker's dozen?", "13"),
        ("What is Spider-Man's real name?", "peter")
    ]

    score = 0

    # question_one = "What is the colour of the sun?"
    # question_two = "Does the sun come out at night?"
    # question_three = "What colour are strawberries?"

    # Intro
    print("Welcome to the quiz.")
    print("Answer the questions to the best of your abilities.")

    time.sleep(2)

    # Ask the questions and get the answer
    for question in questions:
        user_answer = input("\n" + question[0]).strip(" .,?!").lower()

        print("\nChecking response")

        time.sleep(2)

        # See if user's correct
        if user_answer == question[1] and score == 0:
            score += 1
            print("\nyou got it right!, you've gotten " + str(score) + " question right!")
        elif user_answer == question[1] and score >= 1:
            print("\nyou got it right!, you've gotten " + str(score) + " questions right!")
        else:
            print("\nSorry, you are wrong.")






if __name__ == "__main__":
    main()