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

        if Registrations.if_login_exist(login):
            print(f'Login: {login} already axist')
        elif Registrations.validation_password(password):
            print('Password needs contain digits')
        else:
            Registrations._users[login] = {'Login': login, 'Password': password}


class Authorize(Registrations):

    pass


a = Registrations.create_user('kola', 'xpsp2')
b = Registrations.create_user('kola', 'xpsp2')

print(Registrations.get_all_users())
