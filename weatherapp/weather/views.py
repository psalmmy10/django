from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

# Create your views here.
def index (request):
    if  request.method == 'POST':
        city = request.POST ['city']
        api_call =  urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=47cfc7c14bc38dfd6217d7c13e04b30c').read()
        json_data_res = json.loads(api_call)
        data = {
            "country_code": str(json_data_res['sys']['country']),
            "coordinate": str(json_data_res['coord']['lon']) + ' ' + str(json_data_res['coord']['lat']),
            "temp": str(json_data_res['main']['temp'])+'k',
            "pressure": str(json_data_res['main']['pressure']),
            "humidity": str(json_data_res['main']['humidity']),
        }
        
    else:
        city = ''
        data = {}
    return render (request, 'index.html', {'city':city, 'data':data})