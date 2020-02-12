from model import User, Attributes


def create_new_user(client_id):
	
	try:
		User(telegram_id=client_id).save()
	except:
		pass

def set_step(client_id, step):
	user = User.objects.get(telegram_id=client_id)
	user.step = step
	user.save()

def set_user_name(client_id, name):

	user = User.objects.get(telegram_id=client_id)
	user.username = name
	user.save()

def set_user_phone(client_id, phone):

	user = User.objects.get(telegram_id=client_id)
	user.phone_number = phone
	user.save()

def set_user_email(client_id, email):

	user = User.objects.get(telegram_id=client_id)
	user.email = email
	user.save()

def set_user_location(client_id, latitude, longitude):

	user = User.objects.get(telegram_id=client_id)
	latitude_and_longitude = Attributes(latitude=latitude, longitude=longitude)
	user.location = latitude_and_longitude
	user.save()

def set_user_needs(client_id, needs):

	user = User.objects.get(telegram_id=client_id)
	user.needs = needs
	user.save()

def current_state(client_id):
	
	try:
		user = User.objects.get(telegram_id=client_id)
		return user.step
	except Exception as e:
		print(e)
		return 1

def get_user(client_id):

	try:
		user = User.objects.get(telegram_id=client_id)
		return user
	except Exception as e:
		print(e)
		return False


def reset_user(client_id):
	user = User.objects.get(telegram_id=client_id)
	user.delete()