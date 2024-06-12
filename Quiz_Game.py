print("Welcome to the Computer Quiz.")
score = 0
playing = input("Do you want to play? (yes/no) ").strip().lower()

if playing != 'yes':
    print("Maybe next time!")
    quit()

quiz = {
    "1. Who is the father of Computers?": "Charles Babbage",
    "11. Which of the following monitor looks like a television and are normally used with non-portable computer systems?": "CRT",
    "3. What is the full form of CPU?": "Central Processing Unit",
    "4. Which of the following computer language is written in binary codes only?)": "machine language"
}

for key, value in quiz.items():
    answer = input(f"{key} ").strip()
    if answer.lower() == value.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print(f"Your Score: {score}/4.")
print (f"Your Score agverage is : {(score / 4) * 100}%.")

