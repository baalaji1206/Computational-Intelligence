num = int(input("Enter the Number: "))

count = 0
for i in range(num, 0, -1):
    count = count + i

for i in range(0, num):
    for j in range(0, num-i):
        print(count, end="")
        count = count-1
    print()