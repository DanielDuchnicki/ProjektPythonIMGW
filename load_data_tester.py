import unittest

import load_data


class TestLoadData(unittest.TestCase):
	
	def test_2001(self):
		"""przypadek testowy dla ladowania danych z lat 2001-2018
		Zakladamy, ze rok powinien znajdowac sie w pierwszym wierszu danych"""
		station_id = 424
		year = 2001
		temperature_data = load_data.TemperatureData(year, station_id)
		rows = temperature_data.read()
		for row in rows:
			self.assertIn(str(year), row)
			break
	
	def test_1966(self):
		"""przypadek dla ladowania danych z lat 1966-1970"""
		station_id = 424
		year = 1966
		temperature_data = load_data.TemperatureData(year, station_id)
		rows = temperature_data.read()
		years = []
		for row in rows:
			years.append(row[2])
		self.assertIn(str(year), years)
		self.assertIn("1968", years)
		self.assertIn("1969", years)


if __name__ == '__main__':
	unittest.main()
