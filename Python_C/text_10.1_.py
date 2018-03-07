import requests
def getHTMLText(url):  #有一个报错，网络解决办法是加一个参数，但是不明白
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
url = "http://www.baidu.com"
print(getHTMLText(url))
