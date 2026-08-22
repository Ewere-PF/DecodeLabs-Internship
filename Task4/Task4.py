# General Knowledge Quiz
# Project 4 - DecodeLabs Python Programming Internship

print("Welcome to the General Knowledge Quiz!")
print("Answer the following 3 questions.\n")

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Paris.")

# Question 2
answer = input("\n2. How many continents are there in the world? ").strip().lower()

if answer in ["7", "seven"]:
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is 7.")

# Question 3
answer = input("\n3. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The correct answer is Mars.")

# Final Score
print("\nQuiz Completed!")
print(f"Your final score is {score}/3.")

if score == 3:
    print("Excellent! You got all the questions correct!")
elif score == 2:
    print("Good job! You did well.")
elif score == 1:
    print("Not bad! Keep practicing.")
else:
    print("Keep learning and try again!")