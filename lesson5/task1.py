from threading import Thread 

def my_decorator(name_threads, is_daemon):

    def decorator_in(func):

        def wraper(*args):
            print('wraper start')

            t = Thread(target=func, daemon=is_daemon, name=name_threads, args=args)
            t.start()
            print(t.name)

        return wraper

    return decorator_in

@my_decorator(name_threads='my_name_thread', is_daemon=False)
def my_func(*args):
    print(args)


# my_func(1, 2)

# for i in range(10):

#     my_func(i, i+1)

list_download_img_url = ['https://cdn.pixabay.com/photo/2019/12/07/14/57/christmas-tree-4679463_960_720.jpg','https://cdn.pixabay.com/photo/2019/12/07/14/57/christmas-tree-4679463_960_720.jpg']


def download_img(args):
    for i in args:
        print(i)

download_img(list_download_img_url)