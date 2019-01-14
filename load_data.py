import csv


class TemperatureData:
	"""klasa bazowa dla klas obslugujacych pliki z danymi archiwalnymi"""
	
	def __init__(self, year, station_id):
		self.year = year
		self.station_id = station_id
		try:
			NewTemperatureData.__init__(self, year, station_id)
		except FileNotFoundError:
			#Pliki sprzed 2001 roku sa grupowane po 5 lat i maja inna nazwe
			try:
				OldTemperatureData.__init__(self, year, station_id)
			except FileNotFoundError:
				#Plik z 1960 jest wyjatkowy, bo przechowuje dane z 6, a nie 5 lat
				TemperatureData1960.__init__(self, year, station_id)
					
	def read(self):
		'''metoda tworzaca liste wierszy, pobranych z pliku csv,
		ktory znajduje sie w archiwum w katalogu data'''
		rows = csv.reader(self.data)
		return rows

	
class NewTemperatureData(TemperatureData):
	"""klasa obslugujaca archiwa danych temperaturowych z lat 2001-2017
	skladowe: rok, id stacji"""
	
	def __init__(self, year, station_id):
		self.file_name = "data/s_d_{0}_{1}.csv".format(self.station_id, self.year)
		self.data = open(self.file_name, 'r', encoding='ISO-8859-1')
		
		
class OldTemperatureData(TemperatureData):
	"""klasa obslugujaca archiwa z lat 1966-2000
	skladowe: pierwszy_rok, id stacji"""
	
	def __init__(self, year, station_id):
		self.file_name = "data/s_d_{0}_{1}_{2}.csv".format(self.station_id, self.year, self.year + 4)
		self.data = open(self.file_name, 'r', encoding='ISO-8859-1')

	
class TemperatureData1960(TemperatureData):
	"""Klasa dla pliku 1960-1965, ktory jest wyjatkiem i obsluguje 6 lat, a nie 5"""
	def __init__(self, year, station_id):
		self.file_name = "data/s_d_{0}_{1}_{2}.csv".format(self.station_id, self.year, self.year + 5)
		self.data = open(self.file_name, 'r', encoding='ISO-8859-1')
