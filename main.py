from function import Parse

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


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
