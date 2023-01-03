# multiplication game program in python for kids
import random

# generate 10 random multiplication questions
for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    print("Question", i+1, ":", num1, "x", num2, "=")
    user_answer = int(input())

    if user_answer == answer:
        print("Right!")
    else:
        print("Wrong. The answer is", answer)
