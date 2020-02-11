import time
from timeloop import Timeloop
from datetime import timedelta

t = Timeloop()

@t.job(interval=timedelta(secconds=3))
def show():
    print('text')

t.start()