import random
import re
print("Welcome to the HangMan game")
category=["Flowers","Movies","Subjects","ShoppingBrands"]
Flowers=["rose","marigold","lotus","sunflower","lily","tulip","hibiscus"]
Movies=["free","matrix","scoob","interstellar","lucy","argo","maleficent"]
Subjects=["maths","physics","history","chemistry","geography","hindi"]
Shopping_Brands=["zara","veromoda","marks and spencer","gucci","prada","chanel","louis vuitton"]
print(category)
choice=input(("Choose one category: "))
if choice=="Flowers":
    word=random.choice(Flowers)
elif choice=="Movies":
    word=random.choice(Movies)
elif choice=="Subjects":
    word=random.choice(Subjects)
elif choice=="ShoppingBrands":
    word=random.choice(Shopping_Brands)
n=len(word)
# print(word)
# print(n)
print("Your word to guess is : ")
ans="_ "*n
print("_ "*n)
while n!=0 :
    char=input(("Guess a letter: "))
    if word.find(char) != -1:
        indices = [i.start() for i in re.finditer(char, word)]
        # print(indices)
        x=len(indices)-1
        while x>=0:
            i=indices[x]
            x=x-1
            i=i*2
            n=n-1
            ans = ans[:i] + char + ans[i+1:]
            print(ans)
    else:
        print("Wrong choice, Guess another character ")

print("Word Correctly Guessed")