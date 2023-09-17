'''
18-1. requests

requests 라이브러리
    HTTP 요청을 보내기 위한 간편하고 인기있는 라이브러리
    이를 사용하여 웹페이지 데이터를 가져오거나, API와
    상호 작용할 수 있다.
헤더, 바디, IP정보 등등을 내포하고 있는지 등등의 규칙을 정한게 프로토콜이라고 말한다.


라이브러리 설치 방법
pip install requests
터미널에 가서 위 코드를 입력하면 설치가 되기 시작하는 방식을 사용해도 되며
python package를 눌러서 검색창에 입력하고 install package를 눌러서 설치하면 됨
오른쪽 마우스로 소스 코드 보기로 html의 문법으로 기사가 이루어져 있다 <HTML>문서 시작을 알리고,
</HTML>은 문서가 끝이났다는 것이다.
<> </>
헤더: 메타 내용들이 , 본문외의 내용들이 정의가 되어 있음
'''

'''
#프로토콜, 주소, news부터 path 경로인것이다 ? 는 파라미터로도 있음
import requests
url = 'https://www.fnnews.com/news/202309150057411857'
#url = 'https://www.fnnews.com/news/202309150057411857?sid=101' 로 하거나


param = {'sid':'101'}

response = requests.get(url, params= param)
#response = requests.get(url, params= param) 없는 경우에는 param 삭제

print(response.text) #응답의 값을 문자열로 보여달라
'''


import requests
url = 'https://www.fnnews.com/news/202309150057411857'
response = requests.get(url)
print(response.text)