import requests as rq
from bs4 import BeautifulSoup
from bs4 import NavigableString

qUrl = 'https://books.toscrape.com/'

qHeader = {
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}

qResp = rq.get(url=qUrl, headers= qHeader)

# print(qResp.status_code)

bSoup = BeautifulSoup(qResp.content, 'html.parser')

def removeNavigableString(list_data):
    return list(filter(lambda x: type(x) != NavigableString, list_data))

l = removeNavigableString(bSoup.ol.children)

# l_4 = l[4]
L_4 = l[4].h3.a.attrs['title']

print('Title 1 :-' , L_4 )

print('////////////////////////////////')
print('////////////////////////////////')

L_5 = l[5].h3.a.attrs['title']

print('Title 2 :-' , L_5 )

print('////////////////////////////////')
print('////////////////////////////////')

L_6 = l[6].h3.a.attrs['title']

print('Title 3 :-' , L_6 )

print('////////////////////////////////')
print('////////////////////////////////')

L_7 = l[7].h3.a.attrs['title']

print('Title 4 :-' , L_7 )
