import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x = [45, 40, 38, 36, 34, 32, 30, 25, 20]
y = [15.827, 15.489, 15.374, 15.273, 15.191, 15.130, 15.095, 15.168, 15.595]

ax = plt.gca()

ax.set_xlim(15, 50)
ax.set_ylim(15.090, 15.900)

ax.set_xticks([20, 25, 30, 35, 40, 45])
ax.set_yticks([15.1, 15.2, 15.3, 15.4, 15.5, 15.6, 15.7, 15.8, 15.9])

ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

plt.plot(x, y, color='purple', marker='v', markersize=5)
plt.xlabel('расстояние подвеса') 
plt.ylabel('период колебаний') 
plt.title('Зависимость периода колебаний от расстояния подвеса') 

plt.grid(True, which='both')
plt.show()