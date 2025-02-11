import random
import re

class DateError(Exception):
    pass

class Stage:
    def __init__(self, price, start, end, description):
        self.price = price
        self.start = self.set_date(start)
        self.end = self.set_date(end)
        self.description = description
        self.status = 'запланирован'

    def set_date(self, date):
        pattern = r'[0-3]\d\.[0-1]\d\.\d{4}'
        if not re.match(pattern, date):
            raise DateError('Неверный формат даты')
        return date
    
    def next(self):
        if self.status == 'запланирован':
            self.status == 'осуществляется'
        if self.status == 'осуществляется':
            self.status == 'выполнен'
    
    def prev(self):
        if self.status == 'осуществляется':
            self.status == 'запланирован'
        if self.status == 'выполнен':
            self.status == 'осуществляется'
    
    def reject(self):
        self.status == 'забракован'
    
    def start(self):
        self.status == 'осуществляется'
    
    def stop(self):
        self.status == 'выполнен'




class TestDate:
    def test_date_format(self):
        try:
            stage = Stage(100000000, "01.01.1948", "24-01-2023", "Тестовый этап")
        except DateError as e:
            print(f"Тест пройден: {e}")

test = TestDate()
test.test_date_format()