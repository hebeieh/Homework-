import matplotlib.pyplot as plt
import numpy as np

amount = [350, 540, 420, 10, 90, 30]
labels = ["сон", "пары", "домашка", "музыка", "еда", "магазин"]
colors = plt.cm.cool(np.linspace(0, 1, len(amount)))

plt.pie(amount, labels=labels, colors=colors, autopct='%1.f%%')
plt.title("Распорядок дня")
plt.show()