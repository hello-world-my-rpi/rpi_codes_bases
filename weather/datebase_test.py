from get_weather import get_weather
import json


weeks = get_weather()
if weeks:
    with open('weather_date.json','w',encoding='utf-8') as date_base:
        date = json.dumps(weeks)
        date_base.write(date)
else:
    with open('weather_date.json') as date_base:
        date = date_base.read()
        weeks = json.loads(date,encoding='utf-8')


print('-'*70)
for n in range(1,8):
    n = str(n)
    day = weeks[n][1]
    weather = weeks[n][2]
    temp = weeks[n][3]
    if n == '1':
        shidu = weeks[n][4]
        wind = weeks[n][5]
    else:
        shidu = ' '
        wind = ' '
    print("{}           {}    {}    {}    {}".format(day,weather,temp,shidu,wind))
    print('-'*70)
a = input()
