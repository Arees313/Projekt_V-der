import nykeln
import openpyxl
import requests
import json
import datetime
import sys
import time
import pandas as pd
now = datetime.datetime.now()
now_formaterad = now.strftime('%Y-%m-%d')
latitude = 59.30996552541549
longitude = 18.02151508449004
def huvud_meny():
    while True:
        välj = {
            '1': 'Hämta senaste data',
            '2': 'Skriv ut prognos',
            '9': 'Avsluta'

        }
        for key,value in välj.items():
            print(f"{key}. {value}")
        välj_input = input("Välj mellan 1,2 eller 9: ")
        if välj_input not in välj:
            print("Du måste välja mellan 1,2 och 9. ")
            time.sleep(1)
            print("Försök igen!")
            time.sleep(2)
            continue
        else:
            pass
        if  välj_input == '9':
            print("Programmet avslutas..")
            sys.exit()
        elif välj_input == '1':
            huvudmeny_hämta_1()
        elif välj_input == '2':
            skriva_ut_prognos()
            time.sleep(1)
def skriva_ut_prognos():
    while True:
            välj_skriva_ut_prognos = {
                '1': 'Skriv ut prognos från SMHI',
                '2': 'Skriv ut prognos från OMW',
                '3': 'Återgå till förgående meny',
                '9': 'Avsluta'

            }
            for key,value in välj_skriva_ut_prognos.items():
                print(f"{key}. {value}")
            välj_prognos = input("Välj mellan 1,2,3 eller 9: ")
            if välj_prognos not in välj_skriva_ut_prognos:
                print("Du måste välja mellan 1,2,3 eller 9")
                time.sleep(1)
                print("Försök igen!")
                time.sleep(2)
                continue
            if välj_prognos == '9':
                print("Avslutar programmet..")
                sys.exit()

            elif välj_prognos== '1':
                try:
                    data_ur_excel = pd.read_excel('Väder_Samlaren.xlsx')            
                    provider = None
                    for i, x in data_ur_excel.iterrows():
                        titel_väder = x['Provider']

                        if titel_väder != provider:
                            if titel_väder == "SMHI":
                                print(f"Prognos från SMHI {now_formaterad}:")

                            provider = titel_väder
                            timme = None
                            temp = None
                            nederbörd = None

                        if titel_väder == "SMHI":
                            timme = x['Hour']
                            temp = x['Temperature']
                            nederbörd = x['Rain or Snow']
                            nederbörd = str(nederbörd)
                            if nederbörd == "True":
                                nederbörd = "Nederbörd"
                            elif nederbörd == "False":
                                nederbörd = "Ingen nederbörd"
                            timme = f"{timme:02}:00"
                            print(f'{timme} {temp} grader {nederbörd}')
                except: 
                    print("Det finns ingen excelfil tillgänglig, hämta data för att printa ut det!")
                    time.sleep(1)
                    print("Återgår till menyn..")
                    time.sleep(1)
                    continue
            elif välj_prognos== '2':
                try:
                    data_ur_excel = pd.read_excel('Väder_Samlaren.xlsx')            
                    provider = None
                    for i, x in data_ur_excel.iterrows():
                        titel_väder = x['Provider']

                        if titel_väder != provider:
                            if titel_väder == "Openweathermap":
                                print(f"Prognos från Openweathermap {now_formaterad}:")

                            provider = titel_väder
                            timme = None
                            temp = None
                            nederbörd = None

                        if titel_väder == "Openweathermap":
                            timme = x['Hour']
                            temp = x['Temperature']
                            nederbörd = x['Rain or Snow']
                            nederbörd = str(nederbörd)
                            if nederbörd == "True":
                                nederbörd = "Nederbörd"
                            elif nederbörd == "False":
                                nederbörd = "Ingen nederbörd"
                            timme = f"{timme:02}:00"
                            print(f'{timme} {temp} grader {nederbörd}')
                except: 
                    print("Det finns ingen data tillgänglig, hämta data för att printa ut det!")
                    time.sleep(1)
                    print("Återgår till menyn..")
                    time.sleep(1)
                    continue
            elif välj_prognos== '3':
                print("Återgår till förgående meny")
                time.sleep(1)
                break
def huvudmeny_hämta_1():
    while True:
        time.sleep(1)
        välj_2 = {
            '1': 'Hämta data från SMHI',
            '2': 'Hämta data från Openweathermap',
            '3': 'Hämta data från både SMHI och OWM',
            '4': 'Återgå till huvudmeny',
            '9': 'Avsluta'

        }
        for key,value in välj_2.items():
            print(f"{key}. {value}")
        välj_input_2 = input("Välj mellan 1,2,3,4 eller 9: ")
        
        if välj_input_2 == '9':
            print("Programmet avslutas..")
            sys.exit()     
        elif välj_input_2 == '1':
            inhämta_nyhet_smhi()
        elif välj_input_2 == '2':
            hämta_omw()
        elif välj_input_2 == '3':
            inhämta_nyhet_smhi()
            hämta_omw()
        elif välj_input_2 == '4':
            print("Återgår till huvudmenyn..")
            time.sleep(1.5)
            break

api_data = []
def inhämta_nyhet_smhi():
    now = datetime.datetime.now()
    now_formaterad = now.strftime('%Y-%m-%d')
    nu = datetime.datetime.now()
    now_24 = now.strftime('%Y-%m-%d')
    now_24 = now + datetime.timedelta(hours=24)
    url = (f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.021515/lat/59.30996/data.json')
    response = requests.get(url)
    json_data_från_api = json.loads(response.text)
    if json_data_från_api not in api_data:
        api_data.append(json_data_från_api)
        print("Ny data från SMHI inhämtad!")
    else:
        print("Du har begärt duplicerad data från SMHI.")
        return
    time_series_json = json_data_från_api['timeSeries'][:24]
    for time_series in time_series_json:
        for parameter in time_series['parameters']:           
            if parameter['unit'] == 'Cel':
                temp = parameter['values'][0]
                temp_x = str(temp)
            if parameter['name'] == 'pcat':
                nederbörd = parameter['values'][0]      
        while (now < now_24):
            nu111 = now + datetime.timedelta(hours=1)
            now_formaterad = now.strftime('%Y-%m-%d')
            now_hour_formaterad = nu111.strftime('%H')
            now = now + datetime.timedelta(hours=1)
            if nederbörd >= 1:
                result = True
            else:
                result = False
            temp_x = str(temp)
            datan_ur_api = [ 
        [nu, longitude, latitude, now_formaterad, now_hour_formaterad, temp_x, result, "SMHI"]
        
        ]
            for row in datan_ur_api:
                sheet.append(row)
            break
    workbook.save('Väder_Samlaren.xlsx')
    workbook.close()
    print("Excel filen klar!")
    time.sleep(1)
dåvarande_data = []
def hämta_omw():
    url_OMW = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=daily,minute&units=metric&appid={nykeln.api_key}"
    response_json = requests.get(url_OMW)
    data = json.loads(response_json.text)
    ny_data = [(hour['temp'], hour['weather'][0]['main'], hour['dt']) for hour in data['hourly'][1:25]]
    if dåvarande_data and ny_data == dåvarande_data:
        print("Du har begärt duplicerad data från Openweathermap.")
        return
    else:
        print("Ny data från Openweathermap inhämtad!")
        dåvarande_data.clear()
        dåvarande_data.extend(ny_data)
    tillagda_rader = 0
    for hourly in data['hourly'][1:25]:
        for weather in hourly['weather']:
            if weather['main']:
                cloud = weather['main']
                if cloud == "Clouds":
                    cloud = False
                if cloud == "Clear":
                    cloud = False
                if cloud == "Rain":
                    cloud = True
                if cloud == "Snow":
                    cloud = True
            if hourly['dt']:
                datum = hourly['dt']
                formaterad_datum = datetime.datetime.fromtimestamp(datum).strftime('%Y-%m-%d')
            if hourly['temp']:
                temp = hourly['temp']
                temp = str(temp)
            datum_24 = datum
            datum_24_omformatering = datetime.datetime.fromtimestamp(datum_24)
            timme_datum24 = datum_24_omformatering.strftime('%H')
            now = datetime.datetime.now()
        data_ur_OMW = [ 
            [now, longitude, latitude, formaterad_datum, timme_datum24, temp, cloud, "Openweathermap"]
            
        ]
        for row in data_ur_OMW:
            sheet.append(row)
            tillagda_rader += 1   
            if tillagda_rader >= 24:
                break
        if tillagda_rader >= 24:    
            break        
    workbook.save('Väder_Samlaren.xlsx')
    workbook.close()
    time.sleep(1)
    print("Excel filen klar!")
    time.sleep(1)
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
huvud_meny()