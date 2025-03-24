import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig
import os


plt.style.use("/Volumes/kobowmi/!HOME/Info 11/Python/Plotting/dark.mplstyle")

# Data from the image
U1_values = [1,2,3,4,5,6,7,8,9,10]
I1_values = [0.09,0.19,0.29,0.39,0.49,0.59,0.69,0.8,0.9,1]


# Fixed x and y values for the plot as specified by the user
x_fixed = [1,2,3,4,5,6,7,8,9,10]
y_fixed = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]


# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(U1_values,I1_values, marker="o", linestyle="-", color="#f17676", label=r"Versuch 1 (R = 100 $\Omega$)")




# Trendline erstelle nfür die beiden Messungen
# z = np.polyfit(s_values_set_1, F_values, 1)
# p = np.poly1d(z)
# plt.plot(s_values_set_1, p(s_values_set_1), "#DA073B", label="Trendline 1")

# Zweite Trendline
# z = np.polyfit(I2_values, R_values, 1)
# p = np.poly1d(z)
# plt.plot(I2_values, p(I2_values), "#DBA507", label="Trendline 2")

# def exponential_func(x, a, b, c):
#     return a * np.exp(b * x) + c

# Curve-Fit anwenden
# params, covariance = curve_fit(exponential_func, i, t)


# Fixierung der achsen 
plt.yticks(y_fixed)
plt.xticks(x_fixed)

# Labels and title++
plt.ylabel("I in mA")
plt.xlabel(r"U in V")
plt.title("U-I-Diagramm", fontweight="demi", size="18", va="top")

plt.grid(True,ls=":", fillstyle="full")
plt.legend()
plt.draw()

name = os.path.basename(__file__).split(".")[0]

plt.savefig(f"{name}.png", transparent=False, dpi=600)

plt.show()

