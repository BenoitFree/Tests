import unittest
from unittest.mock import MagicMock

from evaluation.exercice4.piscine_function import start_heating


class MyTestCase(unittest.TestCase):
    def test_piscine_temperature_true(self):
        mock = MagicMock()
        mock.get_last_days_temps.return_value = [18, 20.5, 26]
        mock.get_actual_temp.return_value = 27

        start_heating(mock)
        mock.set_heater.assert_called_with(True)

    def test_piscine_wrong_actual_temp(self):
        mock = MagicMock()
        mock.get_last_days_temps.return_value = [18, 20.5, 26]
        mock.get_actual_temp.return_value = 11
        start_heating(mock)
        mock.set_heater.assert_called_with(False)


    def test_piscine_wrong_last_days_temp(self):
        mock = MagicMock()
        mock.get_last_days_temps.return_value = [18, 20.5, 5]
        mock.get_actual_temp.return_value = 27

        start_heating(mock)
        mock.set_heater.assert_called_with(False)


if __name__ == '__main__':
    unittest.main()
