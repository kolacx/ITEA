class Registrations():

    _users = {}

    def validation_password(password):
        
        if not any(char.isdigit() for char in password):
            return True

    def if_login_exist(login):

        if login in Registrations.get_all_users():
            return True

    def get_all_users():
        return Registrations._users

    def create_user(login, password):

        # if Registrations.if_login_exist(login):
        #     print(f'Login: "{login}" already axist')
        # elif Registrations.validation_password(password):
        #     print('Password needs contain digits')
        # else:
            Registrations._users[login] = {'Login': login, 'Password': password}


class Authorize(Registrations):

    def log_in(login, password):
        pass


# Test Authorize log_in() start
a = Registrations.create_user('kola', 'qqq2')

print(Registrations.get_all_users())

print(Authorize.log_in('kola', 'qqq2'))
# Test Authorize log_in() end


def registration():

    login = input('Login: ')

    while Registrations.if_login_exist(login):
        print(f'Login: "{login}" already axist')
        login = input('Login: ')

    password = input('Password: ')

    while Registrations.validation_password(password):
        password = input('Password needs to contain digits. Password: ')
    
    re_password = input('Re_password: ')

    while password != re_password:
        print('Password != re_password')

        password = input('Password: ')

        while Registrations.validation_password(password):
            password = input('Password needs to contain digits. Password: ')
        
        re_password = input('Re_password: ')

    Registrations.create_user(login, password)

    print(Registrations.get_all_users())

def log_in():

    login = input('Enter Login: ')

    if not Registrations.if_login_exist(login):
        print(False)

    users = Registrations.get_all_users()

    password = input('Enter Password: ')

    if users[login]['Password'] == password:
        print(True)


def menu():

    q = input('Registrations or Authorize? (r/a) ')

    if q == 'r':
        registration()
    elif q == 'a':
        log_in()
        

menu()