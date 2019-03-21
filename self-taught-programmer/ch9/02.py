n = input = "What is your name?"
a = input = "What is your purpose?"

with open("answers.txt", "w+") as answer:
    answer.write(n)
    answer.write(a)
