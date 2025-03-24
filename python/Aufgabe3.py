import math

var = int(input("von 1 bis "))

for i in range(1, var + 1):
    print(f"Zahl: {i} >>>  {i}^2 = {i**2: >05} | {i}^3 = {i**3: >05}  | Wurzel aus {i} {math.sqrt(i):>05.2f}")
   