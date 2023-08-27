from concurrent.futures import ThreadPoolExecutor
import random
import threading
import requests
import time
download_list = ["https://images.unsplash.com/photo-1685468412851-228199f688d3?ixlib=rb-4.0.3&dpr=2&auto=format&fit=crop&w=120&h=200&q=60",
                 "https://images.unsplash.com/photo-1682685797660-3d847763208e?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&dl=neom-cYy-o9i8aCs-unsplash.jpg"]

music_list = ["https://aac.saavncdn.com/634/e808fd69b07dd312c532e76e774645e0_160.mp4","https://aac.saavncdn.com/014/5a1c76a6977a2aab6e5bfcc1adbe029f_160.mp4",
              "https://aac.saavncdn.com/981/ff704210de1a556e6d59fe7241f94983_160.mp4"]
conda = ["https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"]
def download_image(url,file_name):
    response = requests.get(url=url,stream=True)
    rand = random.randint(1,1000)
    if(response.headers.get('Content-Type') == 'image/jpeg'):
        with open(f"Downloaded{rand}.jpeg",'wb') as file:
            for i in response.iter_content(chunk_size=10 * 1024):
                print("Downloading Image")
                file.write(i)
                threading.Thread.join()
    elif(response.headers.get('Content-Type')=='audio/mp4'):
        try:
            with open(f"{file_name}.mp3",'wb') as file:
                for i in response.iter_content(chunk_size= 10 * 1024):
                    print("Downloading Music")
                    file.write(i)
        except TypeError as e:
            print("Invalid Type")
    print(response.headers)

def download_conda(url):
    response = requests.get(url,stream=True)
    type = response.headers.get('Content-Type')
    is_exe = url.split('/',4)
    print(is_exe[len(is_exe)-1])
    if type == "application/octet-stream":
        file_name = is_exe[len(is_exe)-1]
        print(float(response.headers.get('Content-Length'))/(1024 * 1024))
        with open(file_name,"wb") as file:
            if(float(response.headers.get('Content-Length'))/(1024 * 1024) > 30.112):
                for chunks in response.iter_content(chunk_size=1024 * 10):
                    print(f'downloading {is_exe[len(is_exe)-1]} ..')
                    file.write(chunks)

if __name__ == '__main__':
    print("QAt maia")
    with ThreadPoolExecutor(max_workers=2) as e:
        for i in range(2):
            file_name = str(input("Enter the file Name: "))
            e.submit(download_image,music_list[i],file_name)