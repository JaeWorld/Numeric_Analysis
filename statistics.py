import numpy as np
import matplotlib.pyplot as plt

mid = np.array([80, 70 ,60, 90])
avg = mid.mean()
var = mid.var()
sd = np.sqrt(var)
var1 = ((mid[0]-avg)**2 + (mid[1]-avg)**2 + (mid[2]-avg)**2 + (mid[3]-avg)**2)
np.sqrt(mid.var())
np.sqrt(var1)

# 난수 생성
n = np.random.randn(10000)

# 정규 분포 (Normal Distribution)
# -1보다크고 1보다 작은 범위에 생기는 난수 비율이 약 68%로 나오는지 확인
print(np.where((n>=-1) & (n<=1)))
print(np.size(np.where((n>=-1) & (n<=1))))
avg = n.mean()  #평균
var = n.var()  #분산
print(avg)
print(var)

# -2보다크고 2보다 작은 범위에 생기는 난수 비율이 약 95%로 나오는지 확인
print(np.where((n>=-2) & (n<=2)))
print(np.size(np.where((n>=-2) & (n<=2))))
avg = n.mean()  #평균
var = n.var()  #분산
print(avg)
print(var)

# 균등 분포 (Uniform Distribution)
# -1보다 크고 1보다 작은 범위에 난수 비율 100% 인지 확인
u = np.random.uniform(-1, 1, 10000)
print(np.size(np.where((u>=-1) & (u<=1))))

plt.figure(2)
plt.hist(n, 10)  # histogram 그래프
plt.show()

s = np.random.uniform(6, 7, 25)
plt.figure(3)
plt.plot(s)
plt.show()

plt.figure(4)
plt.hist(s, 5)
plt.show()
