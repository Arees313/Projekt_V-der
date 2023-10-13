import nykeln
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import alignment
import requests
import json
import datetime
from rich import print_json
def hämta_omw():
    latitude = 59.30996552541549
    longitude =  18.02151508449004
    url_OMW = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=daily,minute&units=metric&appid={nykeln.api_key}"
    response_json = requests.get(url_OMW)
    data = json.loads(response_json.text)
    print(data)
    now = datetime.datetime.now()
    now_24 = now + datetime.timedelta(hours=24)
    lista_med_temp = []


    while (now < now_24):
        for hourly in data['hourly']:
            for weather in hourly['weather']:
                if weather['main']:
                    cloud = weather['main']
                    if cloud == "Clouds":
                        cloud = "Ingen nederbörd"
                    if cloud == "Clear":
                        cloud = "Ingen nederbörd"
                    if cloud == "Rain":
                        cloud = "Nederbörd"
                    if cloud == "Snow":
                        cloud = "Nederbörd"
                if hourly['dt']:
                    datum = hourly['dt']
                    #datum += 7200
                    formaterad_datum = datetime.datetime.fromtimestamp(datum).strftime('%Y-%m-%d %H:%M:%S')
                if hourly['temp']:
                    temp = hourly['temp']
                    lista_med_temp.append(temp)
                    nu111 = now + datetime.timedelta(hours=1)
                    now_hour_formaterad = nu111.strftime('%H')
                    f_print = f"{(lista_med_temp)}°C grader {formaterad_datum} {cloud}"
                    print(f_print)
                data_ur_OMW = [ 
                    [now, longitude, latitude, formaterad_datum, now_hour_formaterad, lista_med_temp, cloud, "Openweathermap"]
                    
                ]
                for row in data_ur_OMW:
                    sheet.append(row)
                workbook.save('Väder_Samlaren.xlsx')
                workbook.close()
                    
        break

try:
    workbook = openpyxl.load_workbook('Väder_samlaren.xlsx')
    sheet = workbook.active
except:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    titlar = [ 
    ['Created', "Longitude", 'Latitude', 'Date', 'Hour', 'Temperature', 'Rain or Snow', 'Provider']


    ]
    for row in titlar:
        sheet.append(row)
    
hämta_omw()
    # while (now < now_24):