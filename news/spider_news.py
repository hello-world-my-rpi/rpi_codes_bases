from urllib import request,parse
import random


def get_url(place='home'):
    url = 'https://news.sina.com.cn/'
    if place == 'home':
        url += 'china/'
    else:
        url += 'world/'
    try:
        proxys = [
                {'HTTPS':'219.234.5.128:3128'},
                {'HTTPS':'218.65.219.119'},
                {'HTTPS':'139.219.8.96'},
                {'HTTPS':'182.35.84.183'},
                {'HTTPS':'123.163.97.187'},
                ]
    
        proxy = random.choice(proxys)    
        proxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_handler)
        response = opener.open(url,timeout=20)
        news_url = response.read().decode('utf-8')[58122:85073]
        return news_url
    except:
        print('Can not open')
        return None

if __name__ == '__main__':print(get_url(''))
