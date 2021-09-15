age = int(input('Enter your age: '))
print(age)

if age > 40:
    print("You are too old to have a pokemon :(")
elif age >= 10:
    print("Choose your pokemon!20")
else:
    print('You have to wait until you are 10 years old.')



final_mark = 79
if final_mark >= 80:
    grade = 'A'
elif final_mark >= 70:
    grade = 'B'
elif final_mark >= 60:
    grade = 'C'
elif final_mark >= 50:
    grade = 'D'
else:
    grade = 'F'
print(f'The Mark is {grade}.')

x = 50
y = 20
max = x if x > y else y

