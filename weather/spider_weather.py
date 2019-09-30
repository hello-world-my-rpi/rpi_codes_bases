from urllib import request,parse


def get_url():
    try:
        url = "https://www.tianqi.com/guangde"
        headers = {
            'User-Agent':'Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.71',
            "Host":'www.tianqi.com'
        }
        rqst = request.Request(url = url,headers = headers,method = 'POST')
        response = request.urlopen(rqst,timeout=20)
        weather_url = response.read().decode('utf-8')
    except:
        print("Can't opem the website")
        return None
    else:
        return weather_url
