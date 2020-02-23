from mongoengine import *

db = connect('my_home_db')


class Curator(Document):
    name = StringField(max_length=256, min_length=0, required=True)


class Facultet(Document):
    name = StringField(max_length=256, min_length=0, required=True)

    def filter_by_facultet(self):
        return Student.objects.filter(
            facultet=self
            )

    def top_by_facultet(self, value):

        student = self.filter_by_facultet()

        top_students = []

        for st in student:
            if sum(st.marks)/len(st.marks) >= value:
                top_students.append(st)

        return top_students

class Student(Document):
    fullname = StringField(max_length=256, min_length=0, required=True)
    group = IntField(max_length=10, min_length=0)
    marks = ListField(IntField(max_length=3, min_length=0))
    
    curator = ReferenceField('Curator')
    facultet = ReferenceField('Facultet')

    @classmethod
    def create_student(cls, **kwargs):
        return cls(**kwargs).save()

    @classmethod
    def read_student(cls, **kwargs):
        return cls.objects.get(**kwargs)

    def update_student(self, **kwargs):
        self.update(**kwargs)

    def deleta_student(self):
        self.delete()


fac = Facultet.objects.get(name='Facultet №2')

for st in fac.filter_by_facultet():
    print(st.fullname)

print('-' * 10)

students = fac.top_by_facultet(55)

for st in students:
    print(st.fullname, st.marks)