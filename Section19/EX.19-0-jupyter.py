'''
Jupyter.py

설치방법
    pip install jupyter

실행방법
    jupyter notebook dobby2025
ctrl + enter: 실행
shift + enter :  실행 후에 공간 추가 num
dd (d 2번은 삭제 )
esc + z undo
esc + a는 위에 새로운 줄이 생긴다
esc+ m 스택이 쌓이지 않는 #
'''

#Figure 객체 생성
figure= plt.figure()

axes = figure. add_subplot(111) #행 열 번호
x= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y= [1200, 800, 500, 400, 700, 800]
axes. plot(x, y, linestyle= '--', marker='^', color = 'red')
plt.show()