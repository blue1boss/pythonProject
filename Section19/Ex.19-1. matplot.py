import matplotlib.pyplot as plt

#Figure 객체 생성
figure= plt.figure()

#멘토 파이선 시리즈
#matplotlib.org/stable/


#axes = figure. add_subplot(111) #행 열 번호
axes = figure. add_subplot(223) #행 열 번호 위치가 달라진다는 것이다
x= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y= [1200, 800, 500, 400, 700, 800]
axes. plot(x, y, linestyle= '--', marker='^', color = 'red')
plt.show()

#하이픈 2개로 하면 점선으로 나오게 됨 , 마커를 포인트 데이터 를 ^모양으로