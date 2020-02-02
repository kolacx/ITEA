class File():

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __enter__(self):
		print(f"Entered args are {self.a, self.b}")
		return "Hello"

	def __exit__(self, *args):
		print("The end of context manager")
		print(args)

with File(1, 4) as f:
	print(1)