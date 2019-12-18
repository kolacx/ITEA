from threading import Thread 
import time

# sinhrone
def testing_threads():
    time.sleep(2)
    print('Func called')


start_time = time.time()
# for i in range(20):
#     testing_threads()

print(time.time() - start_time)

#paralel

# thread_list = []
# start_time = time.time()
# for i in range(20):
#     t = Thread(target=testing_threads, name=f'MyThrea-{i}')
#     t.start()
#     print(t.name)
#     thread_list.append(t)

# може м пихунуть в лист и поочереди его вызвать
# for i in thread_list:
#     print(i.start)

print(time.time() - start_time)


t = Thread(target=testing_threads, daemon=True)
t.start()
# t.join()
print('I am the main thread')