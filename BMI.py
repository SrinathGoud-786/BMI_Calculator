
Height = float(input("Enter your Height in centimeters:"))
Weight = float(input("Enter your Weight in kg:"))
Height = Height/100
BMI = Weight/(Height*Height)
print("Your Body Mass Index is:", BMI)
if(BMI>0):
        if(BMI<=16):
                print("You are severly Underweight")
        elif(BMI<=18.5):
                print("You are Underweight")
        elif(BMI<=25):
                print("You are Healthy")
        elif(BMI<=30):
                print("You are Overweight")
        else:
                print("You are severly Overweight")
else:
        print("Enter Valid Details")