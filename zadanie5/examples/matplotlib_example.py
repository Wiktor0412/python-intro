import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Wykres liniowy - Matplotlib")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.grid(True)
plt.show()
