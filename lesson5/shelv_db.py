import shelve

FILENAME = 'test_db'

# with shelve.open(FILENAME) as db:
#     db['new_key'] = 'New Value'

# with shelve.open(FILENAME) as db:
#     print(db['new_key'])
#     print(db.get('new_key1', 'EMPTY'))

# with shelve.open(FILENAME) as db:
#     print(dict(db.items()))

# with shelve.open(FILENAME) as db:
#     db['new_key'] = {'new value': 1}


class UserDB:

    _instans = None

    def __new__(cls, *args, **kwargs):
        if not cls._instans:
            cls._instans = super().__new__(cls)
            return cls._instans
        else:
            raise NameError('The object already exists')

    def __init__(self, filename):
        self._filename = filename


    def get_db(self):
        return shelve.open(self._filename)

    def create_user(self, **kwargs):
        with shelve.open(self._filename) as db:
            users = db.get('users')

            if not users:
                db['users'] = kwargs
            else:
                users.update(kwargs)
                db['users'] = users

    def get_all_users(self):
        with shelve.open(self._filename) as db:
            return dict(db['users'].items())



db = UserDB(FILENAME)

db.create_user(**{'login': 'password'})
db.create_user(**{'new_login': 'new_password'})

print(db.get_all_users())