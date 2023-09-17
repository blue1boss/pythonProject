'''
BeautifulSoup 라이브러리
    HTML, XML등의 마크업 언어를 파싱하는 라이브러리이다. (패키지를 모아둔 : 모듈 < 패키지 < 라이브러리 )
    ex) <html>텍스트</html>

BeautifulSoup 설치방법
pip install beautifulsoup4


큰 제목만 읽어오는 것을 의미
https://news.nate.com/rank?mid=n100
<h2 class="tit">바다, '도박 파문' 슈에 쓴소리 했다가 멀어져 "다시 돌아오길"…눈물...</h2>볼 수있다

<h2>[단독] "끝까지 간다…난 그런 사람" 尹, 퇴임장관과 4시간30분 만찬</h2> : 작은 기사들은 이렇게 되어 있음을 알 수 있다.
'''

import requests
from bs4 import BeautifulSoup

url = 'https://news.nate.com/rank'
param = {'mid': 'n1000'}
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
tit_list = soup.find_all('h2') #태그에 대한 정보를 list로 돌려달라는 의미인것
for tit in tit_list:
    print(tit.text.strip())

