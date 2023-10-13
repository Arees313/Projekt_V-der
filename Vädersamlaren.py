from ETL_SMHI import inhämta_nyhet_smhi
import pandas as pd
import sys
import datetime
import time
now = datetime.datetime.now()
now_formaterad = now.strftime('%Y-%m-%d')
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
    if välj_input == '1':
        time.sleep(1)
        print("Excel filen skapas..")
        inhämta_nyhet_smhi()
        time.sleep(1)
        print("Excel filen klar!")
        time.sleep(1)
        print("Återgår nu till menyn..")
        time.sleep(1)
        continue
    elif välj_input == '2':
        print("Skriver ut prognos..")
        time.sleep(1)
        print(f"Prognos från SMHI {now_formaterad}:")
        inhämta_nyhet_smhi()
        data_ur_excel = pd.read_excel('Väder_Samlaren.xlsx')
        for index, row in data_ur_excel.iterrows():
            timme = row['Hour']
            temp = row['Temperature']
            nederbörd = row['Rain or Snow']
            timme = f"{timme:02}:00"
            print(f'{timme} {temp} {nederbörd}')
        time.sleep(1)
        print("Återgår till menyn..")
        time.sleep(1)
        continue
    else:
        print("Programmet avslutas..")
        sys.exit()

            

            # workbook = Workbook()
# sheet = workbook.active
# sheet.title = "Sheet"
# path = "test11.xlsx"
# Workbook = openpyxl.load_workbook(path)
# sheet = Workbook.active
# print(f"Prognos från SMHI, {now_formaterad} ")
# loaded_workbook = load_workbook(path)
# loaded_sheet = loaded_workbook["Sheet"]
# for row in loaded_sheet.iter_rows(min_row=2, max_col=7, max_row=25, values_only=True):
#     print(row)