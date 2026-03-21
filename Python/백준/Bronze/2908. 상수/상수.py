number1 , number2  = input().split()

number1 = number1[::-1]
number2 = number2[::-1]

if number1 > number2:
    print(number1)
else:
    print(number2)