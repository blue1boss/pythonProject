'''
beautiful soup.py

URL(Uniform Resource)
    인터넷에서 웹피이지, 이미지, 동영상과 같은 리소스를 찾을 수 있는 주소를 의미한다.
    ex) https://news.nate.com/rank?mid=n100
프로토콜(protocol)
    컴퓨터 네트워크를 통해 통신을 수행하기 위한 규칙, 절차 , 혹은 통신 프로세스를 의미
    ex)
        http/https - 웹서버 프로토콜  (https는 암호화가 되어서 들어간다/ 하나는 되지 않는다)
        ftp - 파일서버 프로토콜
        mailto- 메일서버 프로토콜
        telnet- 원격지 프로토콜

호스트(host)
    리소스가 위치한 서버의 이름
    ex)news.nate.com

포트(port)
    서버에서 사용하는 프로세스의 방번호
    https://news.nate.com:433/rank?mid=n100 중간 443이 생략되어 있는 것을 볼수 있음.
    ex) http - 80 , https - 443이 디폴트 값
    아닌경우는 8080 9090

경로 (path)
    웹서버에서 자원에 대한 경로(물리적 또는 추상적인 경로)
    ex) /rank/ top50.tml

쿼리(query) 또는 파라미터(parameter)  - 추가로 서버에 보내는 데이터
    ex) mid= n1000
'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {'User-Agent': 'Mozila/5.0'}
response = requests.get(url, headers=headers)
html= response.text
soup = BeautifulSoup(html,'html.parser')
news_list = soup.find_all('div', class_='list_content')

for news in news_list:
    news_title = news.text. strip().split('\n')[0]
    print(news_title)

#("./숫자.xlsx")  openpyxl.readthedocs