import time
import sys
import panda as pd
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
                            timme = f"{timme:02}:00"
                            print(f'{timme} {temp} {nederbörd}')
                        elif titel_väder == "Openweathermap":
                            print(f"Prognos från Openweathermap {now_formaterad}:")

                            provider = titel_väder
                            timme = None
                            temp = None
                            nederbörd = None

                        if titel_väder == "Openweathermap":
                            timme = x['Hour']
                            temp = x['Temperature']
                            nederbörd = x['Rain or Snow']
                            timme = f"{timme:02}:00"
                            print(f'{timme} {temp} {nederbörd}')
                except: 
                    print("Det finns ingen excelfil tillgänglig, hämta data för att printa ut det!")
                    time.sleep(1)
                    print("Återgår till menyn..")
                    time.sleep(1)



elif välj_input == '2':
            try:
                data_ur_excel = pd.read_excel('Väder_Samlaren.xlsx')            
                provider = None
                for i, x in data_ur_excel.iterrows():
                    titel_väder = x['Provider']

                    if titel_väder != provider:
                        if titel_väder == "SMHI":
                            print(f"Prognos från SMHI {now_formaterad}:")
                        elif titel_väder == "Openweathermap":
                            print(f"Prognos från Openweathermap {now_formaterad}:")

                        provider = titel_väder
                        timme = None
                        temp = None
                        nederbörd = None

                    if titel_väder == "SMHI":
                        timme = x['Hour']
                        temp = x['Temperature']
                        nederbörd = x['Rain or Snow']
                        timme = f"{timme:02}:00"
                        print(f'{timme} {temp} {nederbörd}')
                    elif titel_väder == "Openweathermap":
                        timme = x['Hour']
                        temp = x['Temperature']
                        nederbörd = x['Rain or Snow']
                        timme = f"{timme:02}:00"
                        print(f'{timme} {temp} {nederbörd}')
            except: 
                print("Det finns ingen excelfil tillgänglig, hämta data för att printa ut det!")
            time.sleep(1)
            print("Återgår till menyn..")
            time.sleep(1)
            continue
