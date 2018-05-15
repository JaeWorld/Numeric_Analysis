import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x1 = np.linspace(0, 10, 50)
# 정의역 0 부터 10까지의 범위에서 50개의 점
x2 = np.linspace(-10, 10, 50)
# 정의역 -10부터 10까지의 범위에서 50개의 점
y1 = x1**3-9*x1**2+24*x1-7
y2 = x2**3-9*x2**2+24*x2-7

# 3차함수 그래프

# figure 1 - x1, y1
plt.figure(1)
plt.plot(x1, y1, '-ro')
plt.grid()
plt.show()

# figure 2 - x2, y2
plt.figure(2)
plt.plot(x2, y2, 'b*-')
plt.grid()
plt.show()

# root(근) 구하기
fx = lambda x: x**3-9*x**2+24*x-7
x = fsolve(fx, 1)
print("Real Root = ", x)

# Real Root =  [ 0.33131491]