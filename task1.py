"""
Аналіз даних Iris: Завантажте дані Iris у DataFrame та проведіть аналіз.
Спробуйте відповісти на такі питання:
Яка середня довжина чашелистика (sepal length) для кожного виду ірису?
Яка максимальна ширина листка (petal width) для виду "setosa"?
Яка розподіленість довжини листка (petal length) для всіх ірисів?
"""

from data_loader import iris_df

mean_sepal_length = iris_df.groupby('class')['sepal_length'].mean()
print(f'Середня довжина чашелистика для кожного виду ірису: \n{mean_sepal_length}')

max_petal_width_setosa = iris_df[iris_df['class'] == 'Iris-setosa']['petal_width'].max()
print(f'\nМаксимальна ширина листка для виду "setosa": \n{max_petal_width_setosa}')

petal_length_distribution = iris_df['petal_length'].describe()
print(f'\nОписова статистика для довжини листка (petal length): \n{petal_length_distribution}')
