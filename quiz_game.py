# ==========================================
#       GENERAL KNOWLEDGE QUIZ GAME
#       Cognifyz Technologies - Task 1
# ==========================================


def play_quiz():

    # List of quiz questions
    questions = [
        {
            "question": "What is the capital of India?",
            "options": [
                "A. Mumbai",
                "B. New Delhi",
                "C. Kolkata",
                "D. Chennai"
            ],
            "answer": "B"
        },

        {
            "question": "Which planet is known as the Red Planet?",
            "options": [
                "A. Earth",
                "B. Venus",
                "C. Mars",
                "D. Jupiter"
            ],
            "answer": "C"
        },

        {
            "question": "How many continents are there in the world?",
            "options": [
                "A. 5",
                "B. 6",
                "C. 7",
                "D. 8"
            ],
            "answer": "C"
        },

        {
            "question": "Which is the largest ocean in the world?",
            "options": [
                "A. Atlantic Ocean",
                "B. Indian Ocean",
                "C. Arctic Ocean",
                "D. Pacific Ocean"
            ],
            "answer": "D"
        },

        {
            "question": "Which is the largest mammal in the world?",
            "options": [
                "A. Elephant",
                "B. Blue Whale",
                "C. Giraffe",
                "D. Hippopotamus"
            ],
            "answer": "B"
        },

        {
            "question": "Which language is primarily used to style web pages?",
            "options": [
                "A. HTML",
                "B. Python",
                "C. CSS",
                "D. SQL"
            ],
            "answer": "C"
        },

        {
            "question": "How many days are there in a leap year?",
            "options": [
                "A. 364",
                "B. 365",
                "C. 366",
                "D. 367"
            ],
            "answer": "C"
        },

        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": [
                "A. China",
                "B. Japan",
                "C. India",
                "D. Thailand"
            ],
            "answer": "B"
        },

        {
            "question": "What is the largest planet in our solar system?",
            "options": [
                "A. Earth",
                "B. Saturn",
                "C. Jupiter",
                "D. Neptune"
            ],
            "answer": "C"
        },

        {
            "question": "Which gas do humans need to breathe?",
            "options": [
                "A. Carbon Dioxide",
                "B. Oxygen",
                "C. Nitrogen",
                "D. Hydrogen"
            ],
            "answer": "B"
        }
    ]

    # Initial score
    score = 0

    # Welcome message
    print("\n==========================================")
    print("        GENERAL KNOWLEDGE QUIZ")
    print("==========================================")
    print("Welcome to the General Knowledge Quiz!")
    print("There are 10 questions.")
    print("Enter A, B, C or D for each question.")
    print("==========================================")

    # Loop through all questions
    for number, question in enumerate(questions, start=1):

        print(f"\nQuestion {number}: {question['question']}")

        # Display options
        for option in question["options"]:
            print(option)

        # Get and validate user answer
        while True:

            answer = input("Your answer (A/B/C/D): ").upper()

            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input!")
                print("Please enter only A, B, C or D.")

        # Check answer
        if answer == question["answer"]:

            print("Correct!")
            score += 1

        else:

            print("Wrong!")
            print(
                f"The correct answer is "
                f"{question['answer']}."
            )

    # Calculate final results
    total_questions = len(questions)
    wrong_answers = total_questions - score
    percentage = (score / total_questions) * 100

    # Display final results
    print("\n==========================================")
    print("              QUIZ COMPLETED")
    print("==========================================")

    print(f"Total Questions : {total_questions}")
    print(f"Correct Answers : {score}")
    print(f"Wrong Answers   : {wrong_answers}")
    print(f"Score           : {score}/{total_questions}")
    print(f"Percentage      : {percentage:.2f}%")

    print("------------------------------------------")

    # Performance message
    if percentage == 100:

        print("Excellent! Perfect score!")

    elif percentage >= 70:

        print("Great job! You performed very well.")

    elif percentage >= 50:

        print("Good effort! Keep practicing.")

    else:

        print("Keep practicing and try again!")

    print("==========================================")


# ==========================================
#              MAIN PROGRAM
# ==========================================

print("\n==========================================")
print("       WELCOME TO QUIZ GAME")
print("==========================================")

while True:

    # Start the quiz
    play_quiz()

    # Ask whether the user wants to play again
    print("\nWould you like to play again?")
    choice = input("Enter Y for Yes or N for No: ").upper()

    if choice == "Y":

        print("\nStarting a new game...")
        print("------------------------------------------")

    elif choice == "N":

        print("\n==========================================")
        print("Thank you for playing!")
        print("Goodbye!")
        print("==========================================")
        break

    else:

        print("\nInvalid choice.")
        print("Game ended.")
        break