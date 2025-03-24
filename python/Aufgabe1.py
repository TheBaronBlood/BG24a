import os

os.system('cls')
#var = int(len(input("Gebe eine Zahl ein: ")))
# print(f"die Zahl hat {var} stellen")

# a = 5 
# b = 3
# a, b = b, a
# print(f"A: {a}; B: {b}")

var = int(input("Gebe eine Zahl ein: "))
if var%2 == 0:  # var modolo (mod)[%] 2
    print("Gerade")
else:
    print("Ungerade")