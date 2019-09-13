from spider_weather import get_url
import re,json

def get_weather():
    url = get_url()
    if url:    
        #---------------------------------------------------------------------------------------------------
        #获得今日的                           湿度       风向      紫外线                              数据。
        pattern_one = '''<dd class="shidu"><b>(.*)</b><b>(.*)</b><b>(.*)</b>'''
        #---------------------------------------------------------------------------------------------------
        #获得今日的                              空气质量        PM            日出      日落          数据。
        pattern_two = '''<dd class="kongqi"><h5.*?>(.*)</h5><h6>(.*)</h6><span>(.*)<br />(.*)</span></dd>'''
        #---------------------------------------------------------------------------------------------------
        #获得日期对应的星期                                              日期        星期
        pattern_three = '''<div class="day7">\n<ul class="week">\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n<li><b>(.*?)</b.*n>(.*)</span>.*?\n'''
        #---------------------------------------------------------------------------------------------------
        #获得每日的天气                              天气
        pattern_four = '''<ul class="txt txt2">\n<li>(.*?)</li>\n<li>(.*?)</li>\n<li>(.*?)</li>\n<li>(.*?)</li>\n<li>(.*?)</li>\n<li>(.*?)</li>\n<li>(.*?)</li>\n'''
        #---------------------------------------------------------------------------------------------------
        #获得每日气温                                                                    最高温   最低温
        pattern_five = '''<div class="zxt_shuju" style="display: none;">\n<ul>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n<li><span>(.*?)</span><b>(.*?)</b></li>\n'''
        #---------------------------------------------------------------------------------------------------


        weeks = {}
        today_date = []#湿度；风向；紫外线；空气质量；PM；日落；日出

        pattern_1 = re.compile(pattern_one)
        pattern_2 = re.compile(pattern_two)
        pattern_3 = re.compile(pattern_three)
        pattern_4 = re.compile(pattern_four)
        pattern_5 = re.compile(pattern_five)


        #湿度、风向、紫外线 数据提取
        result_1 = re.search(pattern_1,url)
        for n in range(1,4):
            today_date.append(result_1.group(n))

        #空气质量、PM、日出、日落 数据提取
        result_2 = re.search(pattern_2,url)
        for n in range(1,5):
            today_date.append(result_2.group(n))
            
        #未来一周的日期提取
        result_3 = re.search(pattern_3,url)
        for n in range(1,14,2):
            data,day = result_3.group(n),result_3.group(n+1)
            weeks[str((n+1)//2)]=[data,day]

        #将未来一周的天气信息整合
        result_4 = re.search(pattern_4,url)
        for n in range(1,8):
            weeks[str(n)].append(result_4.group(n))
            
        #将未来一周的气温区间整合
        result_5 = re.search(pattern_5,url)
        for n in range(1,8):
            highest_t,lowest_t = result_5.group(n*2-1),result_5.group(n*2)
            temp = lowest_t + "-" + highest_t
            weeks[str(n)].append(temp)


        #信息整合，把今日的信息整合到一周信息中
        for each in today_date:
            weeks['1'].append(each)
        
        return weeks
    else:
        return None
