import random
def dice(x):
    switcher={
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
    }
    return switcher.get(x,"Invalid")
x=random.randint(1,6)
print(x)
print(dice(x))