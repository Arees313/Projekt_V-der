import requests
import time
import rich
def kontrollera_data():
    url = (f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/18.021515/lat/59.30996/data.json')
    def hämta_data_smhi():
        return requests.get(url)
    def SMHI_duplicerat(smhi:requests):
        smhi = smhi.json()
        viktig_data = smhi['timeSeries']
        temp_data = []
        for valid in viktig_data[:25]:
            valid['parameters']
            for value in valid['parameters']:
                if value['name'] == 't':
                    temp_data.append((value['values'][0]))
        return temp_data
    cash_data = SMHI_duplicerat(hämta_data_smhi())

    # cash_data = hämta_data_smhi().text
    # cash_data = hämta_data_smhi().json()
    # rich.print_json(data = cash_data)
    new_data = SMHI_duplicerat(hämta_data_smhi())
    time.sleep(5)
    for old,new in zip(cash_data,new_data):
        print(old==new, old, new)
    # new_data = get_important_data(hämta_data_smhi)
    if new_data == cash_data:
        print("Du har hämtat duplicerat data!")
    else:
        print("Uppdaterar ny data till excel filen...")

    # print(cash_data)
    # print(type(cash_data))
kontrollera_data()