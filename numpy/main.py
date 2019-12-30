import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                 header=None)

print(df.iloc[:5, 4])


# setosa와 versicolor를 선택합니다
# y = np.where(y == 'Iris-setosa', -1, 1)
#
# print(y)
# y = df.iloc[0:100, 4].values
