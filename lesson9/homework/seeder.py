from main import Student, Facultet, Curator, db
import random

db.drop_database('my_home_db')

for i in range(10):
	Facultet.objects.create(name=f'Facultet №{i}')

for i in range(10):
	Curator.objects.create(name=f'Curator №{i}')

for i in range(100):
	Student.create_student(
			fullname=f'Sasha {i}',
			group= f'{i*10}',
			marks= [random.randint(1, 100) for i in range(10)],
			curator=Curator.objects.get(name=f'Curator №{random.randint(1, 9)}'),
			facultet=Facultet.objects.get(name=f'Facultet №{random.randint(1, 9)}')
		)