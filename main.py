import random
import time
print("You will get a math question and you have to answer it.")

time.sleep(1.3)

points = 0

def get_number():
    number = random.randint(0, 10000)
    return number

number1 = get_number()
number2 = get_number()

arithmetic_symbol = random.choice(["+", "-", "*", "/"])

if arithmetic_symbol == "+":
    answer = number1 + number2
    user_anwser = input(f"{number1} + {number2} = ")
    if user_anwser == answer:
        print("Correct!")
        print("Points: ", points + 1)
    else:
        print("Incorrect!")

elif arithmetic_symbol == "-":
    answer = number1 - number2
    user_anwser = input(f"{number1} - {number2} = ")
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
    user_anwser = input(f"{number1} * {number2} = ")
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
    user_anwser = input(f"{number1} / {number2} = ")
    if user_anwser == answer:
        print("Correct!")
        print("Points: ", points + 1)
        time.sleep(1.3)
    else:
        print("Incorrect!")
        print("The correct answer is: ", answer)
        print("Points: ", points - 1)
        time.sleep(1.3)
