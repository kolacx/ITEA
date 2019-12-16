from abc import ABC, abstractmethod
import datetime


class Person(ABC):

    @abstractmethod
    def inf_person(self):
        pass

    @abstractmethod
    def age_now(self):
        pass


class Abiturient(Person):

    def __init__(self, sur_name, year_birthday, fac):
        self._sur_name = sur_name
        self._year_birthday = year_birthday
        self._fac = fac

    def inf_person(self):
        print(f'{self._sur_name} {self._year_birthday} {self._fac}')

    def age_now(self):
        now = datetime.datetime.now()
        print(now.year - self._year_birthday)


class Student(Person):

    def __init__(self, sur_name, year_birthday, fac, curs):
        self._sur_name = sur_name
        self._year_birthday = year_birthday
        self._fac = fac
        self._curs = curs

    def inf_person(self):
            print(f'{self._sur_name} {self._year_birthday} {self._fac} {self._curs}')

    def age_now(self):
        now = datetime.datetime.now()
        print(now.year - self._year_birthday)


class Prep(Person):

    def __init__(self, sur_name, year_birthday, fac, dolgnost, stag):
        self._sur_name = sur_name
        self._year_birthday = year_birthday
        self._fac = fac
        self._dolgnost = dolgnost
        self._stag = stag

    def inf_person(self):
            print(f'{self._sur_name} {self._year_birthday} {self._fac} {self._dolgnost} {self._stag}')

    def age_now(self):
        now = datetime.datetime.now()
        print(now.year - self._year_birthday)


a1 = Abiturient('lis1', 1990, 'Python')
a2 = Abiturient('lis10', 1991, 'Python')
a3 = Abiturient('lis20', 1992, 'Python')

s1 = Student('lis2', 1993, 'Python', 1)
s2 = Student('lis100', 1994, 'Python', 1)
s3 = Student('lis1000', 1995, 'Python', 1)

p1 = Prep('lis4', 1996, 'Python', 'head', 10)
p2 = Prep('lis6', 1997, 'Python', 'head', 10)

all_person = [a1, a2, a3, s1, s2, s3, p1, p2]

for i in all_person:
    i.inf_person()

def find_person_age(age):

    for i in all_person:
        if i.age_now >= 10:
            print(f'age greades 10')
            i.inf_person()
