# Question one

# Patient name
name = input("Name of the patient? ")
# Height of patient
height = float(input(f'Please measure the height of {name} in meter squared  '))
# Weight of the patient.
weight = float(input(f'Please measure the weight of {name} in kilogram  '))
# Formula for Body Mass Index
bmi = weight/height
print(f'{name} Body Mass Index is {bmi} kilograms per meter squared')
# Diagnosis
if bmi <= 18.5:
    print(f'{name} you are underweight')
elif 18.5 <= bmi < 25:
    print(f'{name} your weight is normal')
elif 25 <= bmi < 30:
    print(f'{name} you are slightly overweight')
elif 30 <= bmi < 35:
    print(f'{name} you are obese')
else:
    print(f'{name} you are clinically obese!!')

# Question two
# Checking for leap year
year = int(input(f'Please Enter a year: '))
if year %4==0 and (year %100 !=0 or year %400 ==0):
    print("This year is a leap year")
else:
    print("This year is not a leap year")


