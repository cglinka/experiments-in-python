first = [8, 19, 148, 4]
second = [9, 1,  33,  83]
third = []

for index, item in enumerate(first):
    third.append(item * second[index])

print(third)

third_again = []
for f in first:
    for s in second:
        third_again.append(f*s)

print(third_again)
