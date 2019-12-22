import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

x = np.arange(0, 6, 0.1)  # 0부터 6까지 0.1간격으로 리스트 생성
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")
plt.xlabel("x")  # x축 이름
plt.xlabel("y")  # y축 이름
plt.title("sin % cos")
plt.legend()
plt.show()