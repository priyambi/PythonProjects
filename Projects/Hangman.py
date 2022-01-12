import random
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