from spider_news import get_url
import re,time,random


html_home = get_url('home')
html_world = get_url('world')

if html_home or html_world:
    pattern_home = '''<li><a href="https://news.sina.com.cn/.*?>(.*?)</a></li>'''
    pattern_world = '''<h2><a href="http.*?://news.sina.com.cn/.*?target="_blank".*?>(.*?)</a></h2>'''
                       
      
    pt_h = re.compile(pattern_home)
    pt_w = re.compile(pattern_world)

    result_home = re.findall(pt_h,html_home)
    result_world = re.findall(pt_w,html_world)
    print(result_world)    result = result_home + result_world

    while True:
        if input('cmd:')=='n':
            print(random.choice(result))
        else:
            break
        
