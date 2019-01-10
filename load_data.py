import zipfile
import csv
from io import StringIO

class TemperatureData:
	"""klasa obslugujaca archiwa danych temperaturowych z lat 2001-2018
	skladowe: rok, id stacji"""
	
	def __init__(self, year, station_id):
		self.year = year
		self.station_id = station_id

	def read(self):
		"""metoda tworzaca liste wierszy, pobranych z pliku csv,
		ktory znajduje sie w archiwum w katalogu 'data'"""
		zip_path = "data/{0}_{1}_s.zip".format(self.year, self.station_id)
		file_name = "s_d_{0}_{1}.csv".format(self.station_id, self.year)
		zip_file = zipfile.ZipFile(zip_path)
		data = StringIO(zip_file.read(file_name).decode('ISO-8859-1'))
		rows = csv.reader(data)
		return rows
