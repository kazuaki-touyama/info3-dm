import numpy as np

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

import matplotlib.pyplot as plt

# 定義域を設定
x = np.linspace(-1, 1, 100)
y = np.sin(np.pi * x * 0.8) * 10

# グラフの描画
plt.plot(x, y, label='y = sin(pi * x * 0.8) * 10')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = sin(pi * x * 0.8) * 10')
plt.legend()

# グラフを保存
plt.savefig('ex1.1.png')

# グラフを表示
plt.show()
