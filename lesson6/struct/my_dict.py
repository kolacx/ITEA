# get, items, keys, values

class MyDict:

    def __init__(self, **kwargs):
        self._my_dict = dict(**kwargs)
        self._steps = len(kwargs)
        self._current_step = 0

    def get(self, key):
    	if key in self._my_dict:
    		return self._my_dict[key]
    	else:
    		return None

    def items(self):

    	res = []

    	for k in self._my_dict:
    		print(k)
    		print(self._my_dict[k])
    		res.append(tuple((k, self._my_dict[k])))

    	return res

    def keys(self):

    	res = []

    	for k in self._my_dict:
    		res.append(k)

    	return res

    def values(self):

    	res = []

    	for k in self._my_dict:
    		res.append(self._my_dict[k])

    	return res

    def __iter__(self):
        return iter(self._my_dict)

    def __next__(self):
        
        if self._current_step <= self._steps - 1:
            self._current_step += 1
            return next(self._my_dict)

        else:
            raise StopIteration()

    def __add__(d1, d2):

    	new_dict = {}

    	for k in d1:
    		new_dict[k] = d1.get(k)

    	for k in d2:
    		new_dict[k] = d2.get(k)

    	return MyDict(**new_dict)

    def __str__(self):
        return str(self._my_dict)        

a = MyDict(k='v', q='qq', e='ee')
b = MyDict(kk='vv', qq='qqq', ee='eee')

print(a+b)


# print(a)

# print(a.get('c'))

# print(a.items())
# print(a.keys())
# print(a.values())












