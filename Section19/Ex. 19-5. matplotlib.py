'''
19-5
'''

import random
import matplotlib.pyplot as plt

figure= plt.figure()
axes = figure.add_subplot(121)
axes2 = figure.add_subplot(122)

x= [n for n in range(101)] #0부터 100까지
y1 =[]
y2 =[]

for i in range(101):
    y1.append(random.randint(0,100)) #0~100 사이의 난수 추가
    y2.append(random.randint(0,100)) #0~100 사이의 난수 추가

axes.plot(x,y1, color='r', marker='.')
axes2.bar(x,y2,color='g')
plt.show()
