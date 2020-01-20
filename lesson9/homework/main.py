from mongoengine import *


class Curator(Document):
    name = StringField(max_length=256, min_length=0, required=True)


class Facultet(Document):
    name = StringField(max_length=256, min_length=0, required=True)


class Student(Document):
    fullname = StringField(max_length=256, min_length=0, required=True)
    group = IntField(max_length=10, min_length=0)
    marks = ListField(IntField(max_length=3, min_length=0))
    curator = ReferenceField('Curator')
    facultet = ReferenceField('Facultet')

    def create_user(**kwargs):
        return Student(**kwargs).save()

    def fint_student_by_name(name):
        return Student.objects.get(fullname=name)

    def deleta_student(student):
        student.delete()

    def update_student(student, **kwargs):
        student.update(**kwargs)


connect('my_home_db')
# curator = Curator.objects.create(
#     name = 'Curator1'
#     )

# facultet = Facultet.objects.create(
#     name='Prog1'
#     )

my_fucultet = Facultet.objects.get(name='Prog1')
my_curator = Curator.objects.get(name='Curator1')

# student = Student.objects.create(
#         fullname = 'Sasha',
#         group = 123,
#         marks = [1,2,3],
#         curator = my_curator,
#         facultet = my_fucultet
#     )

# student = Student.objects.get(fullname='Sasha')

# st = Student.create_user(
#             fullname = 'Sasha2',
#             group = 123,
#             marks = [1,2,3],
#             curator = my_curator,
#             facultet = my_fucultet
#     )

# st = Student.objects.all()

st = Student.fint_student_by_name('Sasha')

print(st.fullname)

Student.deleta_student(st)

print(Student.objects.all())