from threading import Thread 

class MyThread(Thread):

    def __init__(self, arg, daemon, name):
        self._arg = arg
        super().__init__(daemon=daemon, name=name)

    def runt(self):
        print('workin in thread')


for i in range(100):
    MyThread(1, False, f'name-{i}').start()