import sys

students = []
for i in range(30):
    students.append(i+1)

for ex in range (28):
    stu = int(sys.stdin.readline())
    students.remove(stu)    

print(min(students))
print(max(students))      