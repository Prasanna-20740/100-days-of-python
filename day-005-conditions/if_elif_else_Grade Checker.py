Mark = int(input("Enter Your Mark :"))
if (Mark >= 90 and Mark <=100):
    print ("Your Grade is : A")
elif (Mark >= 80 and Mark <= 89):
    print ("Your Grade is : B")
elif (Mark >=70 and Mark <=79):
    print ("Your Grade is : C")
elif (Mark >=50 and Mark <=69):
    print("Your Grade is : D")
elif (Mark < 50 and Mark >=0):
    print("No Grade Your Fail This Subject Better Luck Next Time")
else:
    print("Invail Marks Enter The Correct Mark __?__/100")
