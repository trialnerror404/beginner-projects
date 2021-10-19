# collection of instructions
# a collection of code



def bmi_calculator():
    name = input("What is your name: ")
    height_m = float(input("How tall are you: "))
    weight_kg = float(input("What is your weight: "))
    bmi = weight_kg / (height_m**2)

    print (f"Hi {name} \nYour BMI is: {bmi}")
    if bmi <= 25:
        print ("You are not overweight")
    elif bmi >= 25:
        print("Your are overweight")

bmi_calculator()
"""

    





print(

"""