import matplotlib.pyplot as plt
plt.style.use("TheBaronBlood/BG24a/python/Plotting/dark.mplstyle")
x = [0, 10, 20, 30]
y = [0, 15, 25, 35]

fig, ax = plt.subplots()
ax.plot(x, y, 'o')  # Punkte plotten

ax.autoscale()  # Automatische Skalierung
ax.margins(0.1)  # 10% Abstand zu den Achsen hinzufügen

plt.show()
