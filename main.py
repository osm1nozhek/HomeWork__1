from function import Parse, parse_cookie

import unittest

class TestParse(unittest.TestCase):
    def test_name(self):
        res = Parse('https://example.com/path/to/page?name=ferret')
        self.assertEqual(res, {'name': 'ferret'})

    def test_color(self):
        res = Parse('https://example.com/path/to/page?color=purple')
        self.assertEqual(res, {'color': 'purple'})

    def test_age(self):
        res = Parse('https://example.com/path/to/page?age=18')
        self.assertEqual(res, {'age': '18'})

    def test_empty1(self):
        res = Parse('http://example.com/')
        self.assertEqual(res, {})

    def test_empty2(self):
        res = Parse('http://example.com/?')
        self.assertEqual(res, {})

    def test_combination1(self):
        res = Parse('https://example.com/path/to/page?name=ferret&age=18')
        self.assertEqual(res, {'name': 'ferret', 'age': '18'})

    def test_combination2(self):
        res = Parse('https://example.com/path/to/page?name=ferret&color=purple')
        self.assertEqual(res, {'name': 'ferret', 'color': 'purple'})

    def test_combination3(self):
        res = Parse('https://example.com/path/to/page?color=purple&age=18')
        self.assertEqual(res, {'color': 'purple', 'age': '18'})

    def test_combination4(self):
        res = Parse('https://example.com/path/to/page?name=ferret&color=purple&age=18')
        self.assertEqual(res, {'name': 'ferret', 'color': 'purple', 'age': '18'})

    def test_combination5(self):
        res = Parse('https://example.com/path/to/page?name=ferret&color=purple&age=18&')
        self.assertEqual(res, {'name': 'ferret', 'color': 'purple', 'age': '18'})


class TestParseCookie(unittest.TestCase):
    def test_name(self):
        res=parse_cookie('name=Dima;')
        self.assertEqual(res, {'name': 'Dima'} )

    def test_double_name(self):
        res = parse_cookie('name=Dima=User;')
        self.assertEqual(res, {'name': 'Dima=User'})

    def test_age(self):
        res=parse_cookie('age=28;')
        self.assertEqual(res, {'age': '28'} )

    def test_colour(self):
        res=parse_cookie('colour=blue;')
        self.assertEqual(res, {'colour': 'blue'} )

    def test_empty1(self):
        res=parse_cookie(' ')
        self.assertEqual(res, {} )

    def test_ua(self):
        res=parse_cookie('колір=blue;')
        self.assertEqual(res, {'колір': 'blue'} )

    def test_combination1(self):
        res=parse_cookie('name=Dima;age=28;')
        self.assertEqual(res, {'name': 'Dima', 'age': '28'} )

    def test_combination2(self):
        res=parse_cookie('name=Dima=User;age=28;')
        self.assertEqual(res, {'name': 'Dima=User', 'age': '28'} )

    def test_combination3(self):
        res = parse_cookie('age=28;colour=blue;')
        self.assertEqual(res, {'age': '28', 'colour': 'blue'})


    def test_combination4(self):
        res=parse_cookie('name=Dima;age=28;colour=blue;')
        self.assertEqual(res, {'name': 'Dima', 'age': '28','colour': 'blue'})


if __name__ == '__main__':
    unittest.main()
