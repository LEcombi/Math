import random
import time
print("You will get a math question and you have to answer it.")
time.sleep(1.3)
times = int(input("How many times do you want to play? "))
dificulty = input("What difficulty do you want? (easy, medium, hard, very hard, impossible) ").lower()

points = 0
times_played = 0
def get_number(dificulty):
    if dificulty == "easy":
        number = random.randint(0, 10)
    elif dificulty == "medium":
        number = random.randint(0, 100)
    elif dificulty == "hard":
        number = random.randint(0, 1000)
    elif dificulty == "very hard":
        number = random.randint(0, 10000)
    elif dificulty == "impossible":
        number = random.randint(0, 100000)
    else:
        print("Invalid difficulty level. Defaulting to easy.")
    return number

while times_played < times:
    number1 = get_number(dificulty)
    number2 = get_number(dificulty)

    arithmetic_symbol = random.choice(["+", "-", "*", "/"])

    if arithmetic_symbol == "+":
        answer = number1 + number2
        user_anwser = int(input(f"{number1} + {number2} = "))
        if user_anwser == answer:
            print("Correct!")
            print("Points: ", points + 1)
        else:
            print("Incorrect!")

    elif arithmetic_symbol == "-":
        answer = number1 - number2
        user_anwser = int(input(f"{number1} - {number2} = "))
        if user_anwser == answer:
            print("Correct!")
            print("Points: ", points + 1)
            time.sleep(1.3)
        else:
            print("Incorrect!")
            print("The correct answer is: ", answer)
            print("Points: ", points - 1)
            time.sleep(1.3)
    elif arithmetic_symbol == "*":
        answer = number1 * number2
        user_anwser = int(input(f"{number1} * {number2} = "))
        if user_anwser == answer:
            print("Correct!")
            print("Points: ", points + 1)
            time.sleep(1.3)
        else:
            print("Incorrect!")
            print("The correct answer is: ", answer)
            print("Points: ", points - 1)
            time.sleep(1.3)
    elif arithmetic_symbol == "/":
        if number2 == 0:
            number2 = 1
        answer = number1 / number2
        user_anwser = int(input(f"{number1} / {number2} = "))
        if user_anwser == answer:
            print("Correct!")
            print("Points: ", points + 1)
            time.sleep(1.3)
        else:
            print("Incorrect!")
            print("The correct answer is: ", answer)
            print("Points: ", points - 1)
            time.sleep(1.3)
    times_played += 1

print("You have played ", times_played, " times.")
print("Your total points are: ", points)
print("Thank you for playing!")