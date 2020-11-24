import requests
from bs4 import BeautifulSoup

class a:
    def game_start(self,iscorrect, first, second):
        #final_received_message = self.final_received_message

        if (first[len(first)-1] == second[0]):
            self.iscorrect = 1
        else:
            self.iscorrect = 2

        return self.iscorrect


first = input("")
second = input("")
iscorrect = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

url = "http://endic.naver.com/search.nhn?query=" + second
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

result = ""
try:
    result += soup.find('dl', {'class': 'list_e2'}).find('dd').find('span', {'class': 'fnt_k05'}).get_text()
except:
    result = "네이버 사전에 등재되어 있지 않습니다."

if(result!="네이버 사전에 등재되어 있지 않습니다."):
    x=a()
    print(x.game_start(iscorrect,first,second))
else:
    print(result)

