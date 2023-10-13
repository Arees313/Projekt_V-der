import requests
url = (f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.021515/lat/59.30996/data.json')

response = requests.get(url)
response = response.text
print(response)

           def hämta_data_smhi():
                return requests.get(url)
            def SMHI_duplicerat(smhi:requests):
                smhi = smhi.json()
                viktig_data = smhi['timeSeries']
                temp_data = []
                for validtime in viktig_data[:25]:
                    validtime['parameters']
                    for value in validtime['parameters']:
                        if value['name'] == 't':
                            temp_data.append((value['values'][0]))
                return temp_data
            cash_data = SMHI_duplicerat(hämta_data_smhi())
            # cash_data = hämta_data_smhi().text
            # cash_data = hämta_data_smhi().json()
            # rich.print_json(data = cash_data)
            time.sleep(10)
            new_data = SMHI_duplicerat(hämta_data_smhi())
            #for old,new in zip(cash_data,new_data):
                #print(old==new, old, new)
            # new_data = get_important_data(hämta_data_smhi)
            if new_data == cash_data:
                print("Du har hämtat duplicerat data!") 
                time.sleep(1)
                print("Excel filen skapas, utan någon uppdaterad data..")
                inhämta_nyhet_smhi()
                time.sleep(1)
                print("Excel filen klar!")
                time.sleep(1)
                print("Återgår nu till menyn..")
                time.sleep(1)
                huvud_meny()