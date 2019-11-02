__author__ = 'hs434'

import unittest
from Calculator import Calculator
from CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
        def setUp(self) -> None:
            self.calculator = Calculator()

        def test_instantiate_calculator(self):
            self.assertIsInstance(self.calculator, Calculator)

        def test_addition(self):
            testdate = CsvReader('/src/Unit_Test_Addition.csv').data
            print(testdate)
            for row in testdate:
             self.assertEqual(self.calculator.add(row['Value 1'],row['Value 2']),int(row['Result']))
             self.assertEqual(self.calculator.result, int(row['Result']))
            pass



if __name__ == '__main__':
    unittest.main()
