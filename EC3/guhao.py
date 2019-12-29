import requests
import queue
from bs4 import BeautifulSoup
import lxml

firstUrl = "https://www.hao123.com/"
urls = queue.Queue()
urls.put(firstUrl)
aim_pages = {}
visited_urls = []

def spide(keyWord):
    while True:
        if urls.empty():
            break
        url = urls.get()
        try:
            page = requests.get(url)
        except:
            # 打印url
            continue
        else:
            soup = BeautifulSoup(page.content, "lxml")

            # 检查是否与主题相关
            title = soup.find("title")
            if title is not None:
                title = title.text
            else:
                title = ""

            if keyWord in title:
                aim_pages[url] = title
            else:
                for meta in soup.find_all('meta'):
                    if "name" not in meta.attrs:
                        continue
                    if meta.attrs["name"] == "keywords":
                        keywords = meta.attrs['content']
                        if keyWord in keywords:
                            aim_pages[url] = title
                        break

            # 新的URl
            for a in soup.find_all('a'):
                if "href" not in a.attrs:
                    continue
                newUrl = a.attrs['href']
                if "http" not in newUrl:
                    continue
                if newUrl not in visited_urls:
                    urls.put(newUrl)

            if len(aim_pages) > 10:
                break


if __name__ == "__main__":
    keyword = input("输入搜索主题：")
    spide(keyword)
    print("搜索结果：")
    i = 0
    for key, value in aim_pages.items():
        i += 1
        print('{i}.{value}     {key}'.format(i=i, key=key, value=value))