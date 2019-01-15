import download_files
import database_helpers
import count_temperature


#Pobierz pliki ze strony, zaladuj do slownika dla stacji Wroclaw i zapisz w pliku storage.pickle
while(True):
    decision = input("Czy chcesz zaktualizować dane? (tak/nie)\n")
    if decision.lower() == "tak":
        print("Pobieram pliki...")
        download_files.download_files(424)
        break
    elif decision.lower() == "nie":
        break
print("Wczytuje...")
database_helpers.create_database(424, 'storage.pickle')
print("Zapisane jako storage.pickle")
#Utworz obiekt przechowujacy dane pobrane z pliku storage i zwracajacy temperatury dla danych dat
temperatures_wroclaw = database_helpers.DatabaseReader('storage.pickle')
#Rob rzeczy na tym obiekcie
print('Srednie temperatury:')
print("- pierwszego dnia wiosny: {0}".format(round(count_temperature.first_days_of_seasons(temperatures_wroclaw)['21/03'], 2)))
print("- pierwszego dnia lata: {0}".format(round(count_temperature.first_days_of_seasons(temperatures_wroclaw)['22/06'], 2)))
print("- pierwszego dnia jesieni: {0}".format(round(count_temperature.first_days_of_seasons(temperatures_wroclaw)['23/09'], 2)))
print("- pierwszego dnia zimy: {0}".format(round(count_temperature.first_days_of_seasons(temperatures_wroclaw)['22/12'], 2)))
print("Jutro przewidujemy {0} stopni, a pojutrze {1}\
".format(round(count_temperature.weather_forecast(temperatures_wroclaw)['tomorrow'],2),
         round(count_temperature.weather_forecast(temperatures_wroclaw)['day after tomorrow'],2)))

#I tak dalej... 
#Raz zainicjowany obiekt temperatures_wroclaw jest przechowywany w pamieci
#Mozemy sie odwolywac do jego metod temperatures_wroclaw.get_temperature(dd_mm_yyyy jako string)
#Oraz temperatures_wroclaw.get_temperatures(dd_mm jako string)
#Pierwszy zwraca nam konkretna temperature jednego konkretnego dnia
#Drugi zwraca namedtuple z temperaturami we wszystkich latach w bazie
