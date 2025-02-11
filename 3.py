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

    def __str__(self):
        return f'{self.description}, {self.status}'

class Project(Stage):
    def __init__(self, price, start, end):
        super().__init__(price, start, end, 'проект')
class Fundament(Stage):
    def __init__(self, price, start, end):
        super().__init__(price, start, end, 'фундамент')
class Walls(Stage):
    def __init__(self, price, start, end):
        super().__init__(price, start, end, 'стены')
class Krisha(Stage):
    def __init__(self, price, start, end):
        super().__init__(price, start, end, 'крыша')
class Electro(Stage):
    def __init__(self, price, start, end):
        super().__init__(price, start, end, 'установка электрооборудования')
class Otdelka(Stage):
    def __init__(self, price, start, end):
        super().__init__(price, start, end, 'отделка')

class Stroika:
    def __init__(self, start, end):
       self.set_date(start)
       self.set_date(end)
       self.start = start
       self.end = end
       self.stages = []
       self.stage_index = 0
       
    
    def set_date(self, date):
        pattern = r'[0-3]\d\.[0-1]\d\.\d{4}'
        if not re.match(pattern, date):
            raise DateError('Неверный формат даты')
        return date

    def add_stage(self, stage):
        self.stages.append(stage)

    def run(self):
        try:
            for i in range(len(self.stages)):
                self.stage_index = i
                stage = self.stages[i]
                stage.start()

                if random.random() < 0.1:
                    stage.reject()
                    raise Exception('Забраковано')
                stage.stop()
                print(f'этап завершен: {stage}')
            return 'стройка завершена успешно'
        except Exception as e:
            print(f'Ошибка {e}')
            if self.stage_index > 0:
                self.stage_index -= 1
                return self.run()
            else:
                return 'стройка отменена'

class TestDate:
    def test_date_format(self):
        try:
            stage = Stage(100000000, "01.01.1948", "24-01-2023", "Тестовый этап")
        except DateError as e:
            print(f"Тест пройден: {e}")

test = TestDate()
test.test_date_format()
stroika = Stroika()