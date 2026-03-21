num = int(input())
count = num

for _ in range(num):
    alp = input()

    for i in range(len(alp)-1):
        if alp[i] == alp[i+1]:
            pass

        elif alp[i] in alp[i+1: ]:
            count -= 1
            break
print(count)