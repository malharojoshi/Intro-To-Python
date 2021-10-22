from random import randint
print("This Is The Guessing Game")
stringNumber=int(input("Please Enter Number That is Between 1 and 9: "))
chance=1
number=randint(1,9)
while chance < 5:
    if stringNumber > number:
        print("Your Number Is Too High")
        chance=chance+1
        stringNumber=int(input("Please Enter Number: "))
    elif stringNumber < number:
        print("Number Is Too Low")
        chance=chance+1
        stringNumber=int(input("Please Enter Number: "))
    else: 
        print("Congratulations You Won")
        break
if stringNumber != number:
    print("You Lose")