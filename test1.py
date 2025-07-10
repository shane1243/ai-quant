import matplotlib
matplotlib.use('TkAgg')  # ✅ 关键：避免 PyCharm 后端报错

import matplotlib.pyplot as plt
import numpy as np

# 模拟生成价格数据
returns = np.random.normal(loc=0.001, scale=0.02, size=100)
prices = 100 * (1 + returns).cumprod()

# 绘图
plt.plot(prices)
plt.title("Simulated Price Path")
plt.xlabel("Days")
plt.ylabel("Price")
plt.grid(True)
plt.show()
