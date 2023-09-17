'''
GetRankPage.py
ctrl F
<strong class="tit_item">
<a href="/moviedb/main?movieId=158260" class="link_txt">오펜하이머</a></strong>
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

url= 'https://movie.daum.net/ranking/boxoffice/weekly'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
movie_list = soup.find_all('strong', class_='tit_item')

#데이터를 저장할 데이터 프레임을 생성
data= {'Rank': [], 'Movie Title': []}


for idx, movie in enumerate(movie_list):
    print(f'{idx+1}위: {movie.text.strip()}')
    data['Rank'].append(idx+1)
    data['Movie Title'].append(movie.text.strip())

#데이터 프레임 객체 생성
df = pd.DataFrame(data)

#openpyxl모듈 필요
df.to_excel('movie_ranking.xlsx', index=False)
print('데이터 엑셀파일로 저장')
