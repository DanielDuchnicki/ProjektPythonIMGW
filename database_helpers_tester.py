import unittest
import pickle
from collections import namedtuple

import database_helpers


DateEntry = namedtuple('DateEntry',['year','temperature'])


class TestDatabaseCreator(unittest.TestCase):
	
	#def test_create_database(self):
		#TODO: poprawic helpers lub test tak, zeby test dzialal
		#'''Test dla tworzenia bazy danych.'''
		#station_id = 424
		#years = (2001, 2002, 2003)
		#test_rows = [[0,0,2001,02,01,0,0,-5],[0,0,2002,06,04,0,0,20.5],[0,0,2003,01,01,0,0,3]]
		#db = DatabaseCreator(years, station_id) #tutaj powinien byc uzyty mock test_rows
		#Self.assertIn('-1.1', db.get_exact_year_temperature("01/02",2001)

	def test_save_to_file(self):
		db = database_helpers.DatabaseCreator([2001],424)
		test_entry =  DateEntry(2001, -2.5)
		test_entry2 = DateEntry(2002, 2)
		db.data = {"01/01":[test_entry, test_entry2]}
		db.save_to_file('db_test.pickle')
		with open('db_test.pickle', 'rb') as f:
			pickle_data = pickle.load(f)
		self.assertEqual(test_entry, pickle_data["01/01"][0])
		self.assertEqual(test_entry2, pickle_data["01/01"][1])

class TestDatabaseReader(unittest.TestCase):

	def test_load_data(self):
		some_data = {"foo":1, "bar":"fgsfds"}
		with open('db_test.pickle', 'wb') as f:
			pickle.dump(some_data, f)
			f.close
		loaded_data = database_helpers.DatabaseReader('db_test.pickle').data
		self.assertEqual(loaded_data['foo'], 1)
		self.assertEqual(loaded_data['bar'], "fgsfds")
		
if __name__ == '__main__':
	unittest.main()

