import unittest

import create_database


class TestCreateDatabaseModule(unittest.TestCase):
	
	def test_create_database(self):
		"""Test dla tworzenia bazy danych.
		Oczekujemy, ze znajdziemy '-1.1' pod kluczem '2001' dla 01/02"""
		station_id = 424
		years = (2001, 2002, 2003)
		raw_temperature_data = load_data.TemperatureData(year, station_id)
		rows = raw_temperature_data.read()
		db = create_database.new(years, station_id)
		Self.assertIn('-1.1', db.get_exact_year_temperature("01/02",2001)

if __name__ == '__main__':
	unittest.main()

