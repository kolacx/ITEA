class MyContextManager():
    def __init__(self, file, flag):
        self.file = file
        self.flag = flag

    def __enter__(self):
        print('CM Start')
        try:
            self.f = open(self.file, self.flag)
        except IOError:
            self.f = open(self.file, "w")
        return self.f

    def __exit__(self, exc_type, exc_value, exc_tr):
        print(exc_type, exc_value, exc_tr)
        if exc_type is IOError:
            self.f.close()
            return True
        self.f.close()

with MyContextManager("file.txt", "w") as f:
    f.write("Hi \n")