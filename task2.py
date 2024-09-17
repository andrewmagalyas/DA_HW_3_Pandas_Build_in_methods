"""
Фільтрація та відбір даних:
Використовуючи pandas, виберіть лише ті дані Iris, які відповідають певним умовам:
Створіть новий DataFrame, в якому будуть лише дані для ірисів виду "versicolor".
Відфільтруйте дані для ірисів з довжиною листка (petal length) більше 5.0.
"""

from main import iris_df

versicolor = iris_df[iris_df['class'] == 'Iris-versicolor']
print(f'Iris versicolor data: \n{versicolor}')

long_petal = iris_df[iris_df['petal_length'] > 5.0]
print(f'\nIrises with petal length > 5.0: \n{long_petal}')