import unittest

import load_data


class TestLoadDataModule(unittest.TestCase):
	
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

if __name__ == '__main__':
	unittest.main()
