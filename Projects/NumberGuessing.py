import random               #randomly generates a number/value


#taking inputs
min=int(input("Enter the minimum value of your range: "))
max=int(input("Enter the maximum value of your range: "))
count=0
x=random.randint(min,max)   #returns a random number

while count>=0:
    y=int(input("Try to Guess the number: "))
    if x==y:
        count=count+1
        print("Congratulations!You have guessed the number correctly in ",count ,"chances")
        break
    elif x>y:
        count=count+1
        print("Guess is too low")
    elif x<y:
        count=count+1
        print("Guess is too high")