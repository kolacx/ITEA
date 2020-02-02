from model import User

user = User.objects.all()

for u in user:
	print(u)