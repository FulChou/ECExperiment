from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error as error
import urllib
import lxml
import re
import random

base_url = "https://baike.baidu.com"
url = "https://baike.baidu.com/item/%E6%96%87%E6%9C%AC%E5%88%86%E6%9E%90"
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html,features='lxml')
for link in soup.find_all('a'):
    print(link.get('href'))

#print(html)

# his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
# url = base_url + his[-1]
#
# html = urlopen(url).read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
# print(soup.find('h1').get_text(), '    url: ', base_url+his[-1])
# if has Chinese, apply decode()
# html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
# print(html)
# soup = BeautifulSoup(html, features='lxml')
# find valid urls
# sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
#
# if len(sub_urls) != 0:
#     his.append(random.sample(sub_urls, 1)[0]['href'])
# else:
#     # no valid sub link found
#     his.pop()
# print(his)
# his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

# for i in range(20):
#     url = base_url + his[-1]
#     try:
#         print(url)
#         print("--------------")
#         urllib.request.urlopen(url, timeout=5)

#     except BaseException:
#         print(error)
#         #print(error.code)
#     html = urlopen(url).read().decode('utf-8')
#     soup = BeautifulSoup(html, features='lxml')
#     print(i, soup.find('h1').get_text(), '   url: ', base_url+his[-1])    
    


#     # find valid urls
#     sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
#     if len(sub_urls) != 0:
#         his.append(random.sample(sub_urls, 1)[0]['href'])
#     else:
#         # no valid sub link found
#         his.pop()