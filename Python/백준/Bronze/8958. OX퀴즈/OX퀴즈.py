import sys
input = sys.stdin.readline
t = int(input())
sum = 0
bonus = 1

for i in range(t):
    qize = list(input().rstrip())

    for j in range(len(qize)):
        if qize[j] == "O":
            sum += bonus
            bonus += 1
        else:
            bonus = 1
            continue
        
    print(sum)
    sum = 0
    bonus = 1       