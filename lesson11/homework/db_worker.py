from model import User

def create_new_user(client_id, step):
	User(telegram_id=client_id,
		step=step).save()

def set_user_name(client_id, name, step):

	user = User.objects.get(telegram_id=client_id)
	user.username = name
	user.step = step
	user.save()

def set_user_phone(client_id, phone, step):

	user = User.objects.get(telegram_id=client_id)
	user.phone_number = phone
	user.step = step
	user.save()

def set_user_email(client_id, email, step):

	user = User.objects.get(telegram_id=client_id)
	user.email = email
	user.step = step
	user.save()

def set_user_location(client_id, location, step):

	user = User.objects.get(telegram_id=client_id)
	user.location = location
	user.step = step
	user.save()

def set_user_needs(client_id, needs, step):

	user = User.objects.get(telegram_id=client_id)
	user.needs = needs
	user.step = step
	user.save()

def current_state(client_id):
	
	try:
		print(client_id, '!!!!!!!!!!!!!!!!!!!!')
		user = User.objects.get(telegram_id=client_id)
		return user.step
	except Exception as e:
		print(e)
		return 1

def get_user(client_id):

	return User.objects.get(telegram_id=client_id)