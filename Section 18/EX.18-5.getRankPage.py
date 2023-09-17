'''
18-5.getrankpage

<p class="title" adult_yn="N"> -> 태그가 타이틀로 되어 있을 것 grouping
    <a href="javascript:;" adultcheckval="1" onclick="bugs.wiselog.area('list_tr_09_chart');bugs.music.listen('6213264',true);
    " title="Love Lee" aria-label="새창">
    Love Lee  : 여기서 텍스트는 A태그 다음에 노래제목이 됨 (조건이 p이고, 타이틀이고, 텍스트인것을 찾아야)
</a>
</p>
'''

import requests
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p', class_='title')
artist_list= soup.find_all('p', class_='artist')

for idx, title in enumerate(music_list):
    #print(type(title)
    #print(type(artist_list[idx]))
    #print(music_list[idx].find_all('a')[0].text.strip(), end='-') 이걸로 하면 깨끗하게 나옴
    #print(title.find_all('a')[0], text.strip(), end='-') 이걸로 해도 깨끗하게 나옴 지금 아래 2번째줄은 대체 하면 됨
    print(idx+1, end='')
    print(title.text.strip(), end='-')
    print(artist_list[idx].find_all('a')[0].text.strip())

    #print(artist_list[idx].text.strip())