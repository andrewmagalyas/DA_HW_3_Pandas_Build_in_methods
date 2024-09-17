import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width",
 "petal_length", "petal_width", "class"]

iris_df = pd.read_csv(url, header=None, names=column_names)

df = pd.DataFrame(iris_df)
