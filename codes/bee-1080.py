bigger = 0
pos = 0

for i in range(3):

    num = int(input())
    if (num > bigger):
        bigger = num
        pos = i + 1

print(bigger)
print(pos)
