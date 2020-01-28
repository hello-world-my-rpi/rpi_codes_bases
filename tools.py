from urllib import request,parse
import re,random

class Weather():
    def __init__(self):
        self.today = self.get_weather()

    def __call__(self):
        self.today = self.get_weather()

    def get_url(self):
        try:
            url = "https://www.tianqi.com/guangde"
            headers = {
                'User-Agent':'Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.71',
                "Host":'www.tianqi.com'
            }
            rqst = request.Request(url = url,headers = headers,method = 'POST')
            response = request.urlopen(rqst,timeout=20)
            weather_url = response.read().decode('utf-8')[9489:11753]
        except:
            print("Can't opem the website")
            return None
        else:
            return weather_url

    def get_weather(self):
        url = self.get_url()
        if url:
            #---------------------------------------------------------------------------------------------------
            #获得今日的                           湿度       风向      紫外线                              数据。
            pattern_one = '''<dd class="shidu"><b>(.*)</b><b>(.*)</b><b>(.*)</b>'''
            #---------------------------------------------------------------------------------------------------
            #获得今日的                              空气质量        PM            日出      日落          数据。
            pattern_two = '''<dd class="kongqi"><h5.*?>(.*)</h5><h6>(.*)</h6><span>(.*)<br />(.*)</span></dd>'''
            #---------------------------------------------------------------------------------------------------
            pattern_three = '''<span><b>(.*)</b>(.*)</span>'''

            today_date = []#湿度；风向；紫外线；空气质量；PM；日落；日出

            pattern_1 = re.compile(pattern_one)
            pattern_2 = re.compile(pattern_two)
            pattern_3 = re.compile(pattern_three)


            #湿度、风向、紫外线 数据提取
            result_1 = re.search(pattern_1,url)
            for n in range(1,4):
                today_date.append(result_1.group(n))

            #空气质量、PM、日出、日落 数据提取
            result_2 = re.search(pattern_2,url)
            for n in range(1,5):
                today_date.append(result_2.group(n))

            #今日天气提取: 天气、最低温、最高温
            result_3 = re.search(pattern_3,url)
            for n in range(1,3):
                today_date.append(result_3.group(n))

            return today_date
        else:
            return ['No date' for i in range(9)]

class News():
    def __init__(self):
        self.news = list(self.get_news())

    def __call__(self):
        self.news = self.get_news()

    def get_news(self):
        html_home = self.get_url('home')
        html_world = self.get_url('world')

        if html_home or html_world:
            pattern_home = '''<li><a href="https://news.sina.com.cn/.*?>(.*?)</a></li>'''
            pattern_world = '''<h2><a href="http.*?://news.sina.com.cn/.*?target="_blank".*?>(.*?)</a></h2>'''

            pt_h = re.compile(pattern_home)
            pt_w = re.compile(pattern_world)

            result_home = re.findall(pt_h,html_home)
            result_world = re.findall(pt_w,html_world)
            result = result_home + result_world

            return result

    def get_url(self,place='home'):
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


