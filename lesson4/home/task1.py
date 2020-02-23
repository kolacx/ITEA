from abc import ABC, abstractmethod
import datetime


class Person(ABC):

    def __init__(self, sur_name, year_of_birthday, faculty):
        self._sur_name = sur_name
        self._year_of_birthday = int(year_of_birthday)
        self._faculty = faculty

    @abstractmethod
    def inf_person(self):
        pass

    @abstractmethod
    def age_now(self):
        pass


class Enrollee(Person):

    def __init__(self, sur_name, year_of_birthday, faculty):
        super().__init__(sur_name, year_of_birthday, faculty)

    def inf_person(self):
        print(f'{self._sur_name} {self._year_of_birthday} {self._faculty}')

    def age_now(self):
        now = datetime.datetime.now()
        return now.year - self._year_of_birthday


class Student(Person):

    def __init__(self, sur_name, year_of_birthday, faculty, course):
        super().__init__(sur_name, year_of_birthday, faculty)
        self._course = course

    def inf_person(self):
        print(f'{self._sur_name} {self._year_of_birthday} {self._faculty} {self._course}')

    def age_now(self):
        now = datetime.datetime.now()
        return now.year - self._year_of_birthday


class Teacher(Person):

    def __init__(self, sur_name, year_of_birthday, faculty, position, experience):
        super().__init__(sur_name, year_of_birthday, faculty)
        self._position = position
        self._experience = experience

    def inf_person(self):
        print(f'{self._sur_name} {self._year_of_birthday} {self._faculty} {self._position} {self._experience}')

    def age_now(self):
        now = datetime.datetime.now()
        return now.year - self._year_of_birthday


enrollee = [Enrollee(f'lis1{i}', f'199{i}', 'Python') for i in range(10)]
student = [Student(f'lis2{i}', f'198{i}', 'Python', i) for i in range(5)]
teacher = [Teacher(f'lis3{i}', f'197{i}', 'Python', 'head', i) for i in range(3)]

all_p = enrollee + student + teacher

for i in all_p:
    i.inf_person()

print('*' * 10)

def find_person_age(age_l, age_h):

    result = [i for i in all_p if i.age_now() >= age_l and i.age_now() <= age_h]

    print(f'Person between range: {age_l} and {age_h}')
    
    for i in result:
        i.inf_person()


find_person_age(22, 46)