import matplotlib.pyplot as plt
import numpy as np

x = ['Продукты', 'Транспорт', 'Техника', 'Мобильная связь', 'Культура и искусство', 'Такси']
y = [17500, 13000, 8500, 1900, 900, 520]

colors = plt.cm.viridis(np.linspace(0, 1, len(x)))
plt.bar(x, y, label='Выписка из банка', alpha=0.2, color=colors)
plt.xlabel('Категории')
plt.xticks(rotation=45)
plt.ylabel('Сумма')
plt.title('Расходы за месяц')
plt.legend(loc='upper right')
plt.show()
