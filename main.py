import download_files
import database_helpers
import count_temperature


#Pobierz pliki ze strony, zaladuj do slownika dla stacji Wroclaw i zapisz w pliku storage.pickle
print("Pobieram pliki...")
download_files.download_files(424)
print("Wczytuje...")
database_helpers.create_database(424, 'storage.pickle')
print("Zapisane jako storage.pickle")
#Utworz obiekt przechowujacy dane pobrane z pliku storage i zwracajacy temperatury dla danych dat
temperatures_wroclaw = database_helpers.DatabaseReader('storage.pickle')
#Rob rzeczy na tym obiekcie
print("Srednie temperatury pierwszego dnia wiosny, lata, jesieni i zimy \
 we Wroclawiu wynosza:{}".format(count_temperature.first_days_of_seasons(temperatures_wroclaw)))
print("Jutro przewidujemy {1} stopni, a pojutrze {2}\
".format(count_temperature.weather_forecast(temperatures_wroclaw)[0], count_temperature.weather_forecast(temperatures_wroclaw)[1]))

#I tak dalej... 
#Raz zainicjowany obiekt temperatures_wroclaw jest przechowywany w pamieci
#Mozemy sie odwolywac do jego metod temperatures_wroclaw.get_temperature(dd_mm_yyyy jako string)
#Oraz temperatures_wroclaw.get_temperatures(dd_mm jako string)
#Pierwszy zwraca nam konkretna temperature jednego konkretnego dnia
#Drugi zwraca namedtuple z temperaturami we wszystkich latach w bazie
