import load_data
import pickle
from collections import namedtuple

DateEntry = namedtuple('DateEntry',['year','temperature'])

class DatabaseCreator:
	"""Obiekty tej klasy przechowuja slownik z danymi z danych lat.
	Udostepnia metody pozwalajace na zaciagniecie danych do slownika i zapisania go do pliku"""
			
	def __init__(self, years, station_id):
		self.station_id = station_id
		self.years = years
		self.data = self._collect_data()
		
	def _collect_data(self):
		'''dodaje do slownika data kolejne rekordy
		kluczem jest data w formacie dd/mm
		wartoscia jest lista named tupli, ktore zawieraja informacje o roku'''
		data = {}
		for year in self.years:
			temperature_data = load_data.TemperatureData(year, self.station_id)
			rows = temperature_data.read()
			for row in rows:
				date_ddmm = "{0}/{1}".format(row[4],row[3])
				year = row[2]
				temperature = row[7]
				row_entry = DateEntry(year, temperature)
				try:
					data[date_ddmm].append(row_entry) 
				except KeyError:
					data[date_ddmm] = [row_entry]
		return data
		
	def save_to_file(self, file_name):
		'''zapisuje slownik z danymi do pliku data.pickle'''
		with open(file_name, 'wb') as f:
			pickle.dump(self.data, f)
			f.close()

class DatabaseReader:
	"""Obiekt tej klasy przechowuje dane pobrane ze slownika pickle
	Udostepnia tez metody umozliwiajace dostep do tych danych"""
	
	def __init__(self, file_name):
		self.file_name = file_name
		self.data = self._load_data()
		
	def _load_data(self):
		with open(self.file_name, 'rb') as f:
			data = pickle.load(f)
		return data
	
	def get_temperatures(self, date_ddmm):
		return self.data[date_ddmm]
