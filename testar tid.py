import datetime
tid = 1697025600
datetime_object = datetime.datetime.fromtimestamp(tid)
total_seconds = (datetime_object - datetime.datetime(1970, 1, 1)).total_seconds()
print(datetime_object)

  # try: data_ur_excel = pd.read_excel('Väder_Samlaren.xlsx')

    # except:
    #     pass
    # try: temp_list = data_ur_excel['Temperature'].tolist()

    # except:
    #     pass
    now = datetime.datetime.now()
    now_formaterad = now.strftime('%Y-%m-%d')
    nu = datetime.datetime.now()
    now_24 = now.strftime('%Y-%m-%d')
    now_24 = now + datetime.timedelta(hours=24)
    latitude = 59.30996552541549
    longitude = 18.02151508449004
    url = (f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.021515/lat/59.30996/data.json')
    response = requests.get(url)
    json_data_från_api = json.loads(response.text)
    if json_data_från_api not in api_data:
        api_data.append(json_data_från_api)
        print("Ny data från SMHI inhämtad!")
    else:
        print("Du har begärt duplicerad data.")
        huvudmeny_hämta_1()
    värde = 0
    lista_med_temp = []
    time_series_json = json_data_från_api['timeSeries'][:24]
    for time_series in time_series_json:
        for parameter in time_series['parameters']:           
            if parameter['unit'] == 'Cel':
                temp = parameter['values'][0]
                temp_x = str(temp) + 'C'
                lista_med_temp.append(temp_x)
            if parameter['name'] == 'pcat':
                nederbörd = parameter['values'][0]
                lista_med_regn.append(nederbörd)        
        while (now < now_24):
            nu111 = now + datetime.timedelta(hours=1)
            now_formaterad = now.strftime('%Y-%m-%d')
            now_hour_formaterad = nu111.strftime('%H')
            now = now + datetime.timedelta(hours=1)
            if nederbörd >= 1:
                parameter['name'] == 'pcat' and värde <= 1
                result = True
            else:
                result = False
            temp_x = str(temp) + 'C'
            datan_ur_api = [ 
        [nu, longitude, latitude, now_formaterad, now_hour_formaterad, temp_x, result, "SMHI"]
        
        
        ]
            for row in datan_ur_api:
                sheet.append(row)
            break
    # if temp_list == lista_med_temp:
    #     print("Duplicerad data kan inte implementeras, återgår till menyn..")
    #     lista_med_temp.clear()
    #     huvudmeny_hämta_1()
    # else:
    #     print("Excel filen skapas, ny data implementeras..")
    #     time.sleep(1)