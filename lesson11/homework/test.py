from model import User

user = User.objects.all()

for u in user:
	# print(u.telegram_id,
 #    u.step,
 #    u.username,
 #    u.phone_number,
 #    u.location,
 #    u.needs,
 #    u.email)
    u.delete()