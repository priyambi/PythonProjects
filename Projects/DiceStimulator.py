import random
def dice(x):
    switcher={
        1:print("It is 1"),
        2:print("It is 2"),
        3:print("It is 3"),
        4:print("It is 4"),
        5:print("It is 5"),
        6:print("It is 6"),
    }
    return switcher.get(x,"Invalid")
x=random.randint(1,6)
#print(x)
dice(x)