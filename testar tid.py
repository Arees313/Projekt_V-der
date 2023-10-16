import datetime
tid = 1697457600
datetime_object = datetime.datetime.fromtimestamp(tid)
total_seconds = (datetime_object - datetime.datetime(1970, 1, 1)).total_seconds()
print(datetime_object)


    # if temp_list == lista_med_temp:
    #     print("Duplicerad data kan inte implementeras, återgår till menyn..")
    #     lista_med_temp.clear()
    #     huvudmeny_hämta_1()
    # else:
    #     print("Excel filen skapas, ny data implementeras..")
    #     time.sleep(1)