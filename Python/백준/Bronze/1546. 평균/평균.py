import sys
n = int(sys.stdin.readline()) 
score = list(map(int, sys.stdin.readline().split()))
m = max(score)
score1 = []

for _ in range(n):
        score1.append(score[_]/m*100)

print(sum(score1)/n)