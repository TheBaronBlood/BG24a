import os

try:
  import numpy
except ImportError:
  print("Trying to Install required module: requests\n")
  os.system('python -m pip install numpy')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import numpy as np

try:
  import matplotlib
except ImportError:
  print("Trying to Install required module: requests\n")
  os.system('python -m pip install matplotlib')
# -- above lines try to install requests module if not present
# -- if all went well, import required module again ( for global access)
import matplotlib.pyplot as plt

import math as m



# os.system("cls")
# A = int(input("A: "))
# os.system("cls")
# B = int(input("B: "))
# os.system("cls")
# C = int(input("C: "))
# os.system("cls")

A, B, C = 3, 5, -4


x1 =  (-B + m.sqrt(B**2 -4*A*C))/(2*A)
x2 =  (-B - m.sqrt(B**2 -4*A*C))/(2*A)

print(f"a: {A}; b: {B}; c:{C}")
print(f"x1 = {x1};  x2 = {x2}")

x_mid = (x1 + x2) / 2

def quadratic_function(x): 
    return A*x**2 + B*x + C # x-Werte festlegen 
x = np.linspace((x2-5), (x1+5), 400) # y-Werte berechnen 
y = quadratic_function(x)

fig, ax = plt.subplots()
plt.plot(x,y)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

plt.plot(x1,0, marker="o", ls="None", color='#f17676')
plt.plot(x2,0, marker="o", ls="None", color='#f17676')


plt.text(x1,2,str(round(x1,2)))
plt.text(x2,2,str(round(x2,2)))


plt.xlim((x1-8),(x2+8))
plt.ylim(-20,50)


plt.grid(True, ls=":", fillstyle="full")

plt.show()

