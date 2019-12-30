from threading import Thread 
import requests

def my_decorator(name_threads, is_daemon):

    def decorator_in(func):

        def wraper(url_list):
            
            thread_list = {}

            for i, url in enumerate(url_list):

                t = Thread(target=func, daemon=is_daemon, name=f'name_threads-{i}', args=(url, i))
                thread_list[i] = {url: t}
                # thread_list.append(t)

            # print(thread_list)

            for i in thread_list:
                for key, value in thread_list[i].items():
                    value.start()
                    print(f'Thread {value.name} started with url - {key}')

            for i in thread_list:
                for key, value in thread_list[i].items():
                    value.join()

        return wraper

    return decorator_in


list_download_img_url = ['https://eoimages.gsfc.nasa.gov/images/imagerecords/74000/74393/world.topo.200407.3x5400x2700.jpg' for i in range(10)]

@my_decorator(name_threads='my_name_thread', is_daemon=False)
def download_img(url, name_num):
    
    img_data = requests.get(url).content

    with open(f'{name_num}-image.jpg', 'wb') as handler:
        handler.write(img_data)
    
    print(f'Download finish {name_num}')


download_img(list_download_img_url)