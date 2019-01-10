"""Ten modul tworzy slownik zawierajacy dane pogodowe pogrupowane po dacie dd/mm"""

import load_data


station_id = 424
years = (2001, 2002, 2003)

DATA = {}

def collect_temperatures_by_year(years, station_id):
	for year in years:
		temperature_data = load_data.TemperatureData(year, station_id)
		rows = temperature_data.read()
		for row in rows:
			date_ddmm = "{0}/{1}".format(row[4],row[3])
			year = row[2]
			temperature = row[7]
			#try:
				#dodac kod, ktory bedzie dopisywal wartosci 
			#except KeyError:
				#lub tworzyl nowy wpis jesli jeszcze nie ma
collect_temperatures_by_year(years,station_id)
		
		
