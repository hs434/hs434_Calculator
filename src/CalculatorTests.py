__author__ = 'hs434'

import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from decimal import getcontext, Decimal

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

        def test_subtraction(self):
            testdata = CsvReader('/src/Unit_Test_Subtraction.csv').data
            print(testdata)
            for row in testdata:
             self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
             self.assertEqual(self.calculator.result, int(row['Result']))
            pass

        def test_multiplication(self):
            testdata = CsvReader('/src/Unit_Test_Multiplication.csv').data
            print(testdata)
            for row in testdata:
             self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
             self.assertEqual(self.calculator.result, int(row['Result']))

        def test_division(self):
            testdata = CsvReader('/src/Unit_Test_Division.csv').data
            print(testdata)
            for row in testdata:
             if row['Value 1'] > row['Value 2']:
                getcontext().prec = 8
             else:
                getcontext().prec = 10
            self.assertEqual(self.calculator.divide(Decimal(row['Value 1']), Decimal(row['Value 2'])), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, Decimal(row['Result']))
            pass



if __name__ == '__main__':
    unittest.main()
