import matplotlib.pyplot as plt

x = ['Продукты', 'Транспорт', 'Техника', 'Мобильная связь', 'Культура и искусство', 'Такси']
y = [17500, 13000, 8500, 1900, 900, 520]

plt.bar(x, y, label='Выписка из банка', alpha=0.1 )
plt.plot(x, y, color='purple', marker='o', markersize=7)
plt.xlabel('Категории')
plt.ylabel('Сумма')
plt.title('Расходы за месяц')
plt.legend(loc='upper right')
plt.show()
