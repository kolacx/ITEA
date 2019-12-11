class Singletone:

    _objects = None

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        if cls._objects:
            # return cls._objects
            raise Exception('Object already axist') # зачем возвращать если можно вызвать ошибку и пусть пользователь отлавливает ее сам

        obj = super().__new__(cls, *args, **kwargs)
        cls._objects = obj
        return obj


obj_1 = Singletone()

obj_2 = Singletone()

print(obj_1, obj_2)