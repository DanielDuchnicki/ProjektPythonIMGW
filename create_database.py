"""Ten modul tworzy slownik DATA zawierajacy dane pogodowe pogrupowane po dacie dd/mm"""

import load_data
import pickle
from collections import namedtuple

station_id = 424
years = (2001, 2002, 2003)
DATA = {}
DateEntry = namedtuple('DateEntry',['year','temperature'])

def collect_temperatures(years, station_id):
	'''dodaje do slownika DATA kolejne rekordy
	kluczem jest data w formacie dd/mm
	wartoscia jest lista named tupli, ktore zawieraja informacje o roku'''
	for year in years:
		temperature_data = load_data.TemperatureData(year, station_id)
		rows = temperature_data.read()
		for row in rows:
			date_ddmm = "{0}/{1}".format(row[4],row[3])
			year = row[2]
			temperature = row[7]
			row_entry = DateEntry(year, temperature)
			try:
				DATA[date_ddmm].append(row_entry) 
			except KeyError:
				DATA[date_ddmm] = [row_entry]

def save_dict_to_file():
	'''zapisuje slownik DATA do pliku data.pickle'''
	with open('data.pickle', 'wb') as f:
		pickle.dump(DATA, f)
		f.close()
				
if __name__ == '__main__':
	collect_temperatures(years,station_id)
	save_dict_to_file()
