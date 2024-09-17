"""
Групування та агрегація:
Використовуючи групування та агрегацію даних, відповідь на такі питання:
Яка середня ширина листка (petal width) для кожного виду ірису?
Яка мінімальна довжина чашелистика (sepal length) для кожного виду ірису?
Скільки ірисів кожного виду мають довжину листка (petal length) більше за середню довжину листка всіх ірисів?
Ці завдання дозволяють вам практикувати основні операції з даними, фільтрацію,
групування та агрегацію, які можна виконати за допомогою бібліотеки pandas на прикладі даних Iris.
"""

from main import iris_df

avg_petal_width = iris_df.groupby('class')['petal_width'].mean()
print(f'Середня ширина пелюстки для кожного виду ірису: \n{avg_petal_width}')
print('\n')

min_sepal_length = iris_df.groupby('class')['sepal_length'].min()
print(f'Мінімальна довжина чашелистика для кожного виду ірису: \n{min_sepal_length}')
print('\n')

avg_petal_length = iris_df['petal_length'].mean()

iris_df['above_avg_petal_length'] = iris_df['petal_length'] > avg_petal_length

above_avg_count = iris_df.groupby('class')['above_avg_petal_length'].sum()

print(f'Кількість ірисів кожного виду з довжиною пелюстки більше за середню ({avg_petal_length:.2f}): \n{above_avg_count}')




