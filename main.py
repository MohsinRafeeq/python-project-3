height = float(input("Enter your height in meter's: \n"))
weight = float(input("Enter your weight in kg: \n"))
bmi = round(weight / height ** 2)
# 5.7 = 6
if bmi < 18.5:
    print(f"your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"your BMI is{bmi}, you have a normal Weight")
elif bmi < 30:
    print(f"your BMI is{bmi}, you are slightly over Weight")
elif bmi < 53:
    print(f"your BMI is{bmi}, you are obese")
else:
    print(f"your BMI is {bmi}, you are Clinically obese.")
