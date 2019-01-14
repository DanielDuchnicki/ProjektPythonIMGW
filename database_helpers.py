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
		'''metoda, ktora zwraca tablice obiektow typu namedtuple,
		zawierajacych informacje o tym jaka temperatura byla
		w poszczegolnych latach dnia, ktory zostal przekazany jako jej argument'''
		return self.data[date_ddmm]
	
	def get_temperature(self, date_ddmmyyyy):
		searched_year = int(date_ddmmyyyy[-4:])
		searched_date_ddmm = date_ddmmyyyy[:5]
		all_rows = self.get_temperatures(searched_date_ddmm)
		for row in all_rows:
			if row.year == searched_year: break;
		return row.temperature


def create_database(station_id, storage_file_name):
	"""Tworzy plik pickle z danymi dla stacji z argumentu station_id
	Plik wynikowy ma nazwe taka, jak przekazano w storage_file_name"""
	# Pliki z lat 1966-2000 sa pogrupowane w plikach po 5 lat
	years = [1960, 1966, 1971, 1976, 1981, 1986, 1991, 1996]
	# Od 2001 kazdy rok jest w osobnym pliku
	for year in range(2001,2017):years.append(year);
	DatabaseCreator(years, station_id).savetofile(storage_file_name)

if __name__ == '__main__':
	#stworzenie pliku pickle (pseudo-bazy danych) z danymi dla Wroclawia
	create_database(424, 'example_db.pickle')
	#przyklady odczytania z tego pliku mozna znalezc w testach dla tego modulu
	
