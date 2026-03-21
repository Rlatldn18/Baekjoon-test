score_dict = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
credit_sum = 0
creditgpa_sum = 0

for _ in range(20):
    sub, credit, gpa = input().split()
    if gpa != "P":
        credit_sum +=  float(credit)
        creditgpa_sum += float(credit) * score_dict[gpa]

print(creditgpa_sum/credit_sum)