import asyncio
import tqdm
import requests
import random
# from pygame import mixer
import os
async def main():
    global counter
    print("Pranjal")
    task = asyncio.create_task(foo("task is created"))
    await asyncio.sleep(11)
    print("Hello Worldf")

async def foo( txt ):
    print(txt)
    await asyncio.sleep(10)
    print("Welcome Back")

music_list = ["https://aac.saavncdn.com/634/e808fd69b07dd312c532e76e774645e0_160.mp4","https://aac.saavncdn.com/014/5a1c76a6977a2aab6e5bfcc1adbe029f_160.mp4",
              "https://aac.saavncdn.com/981/ff704210de1a556e6d59fe7241f94983_160.mp4"]

image_url  = ["https://images.unsplash.com/photo-1573994440949-12f06ada6c4c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDR8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=400&q=60",
              "https://images.unsplash.com/photo-1691832626202-34b24e3bc206?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDV8fHxlbnwwfHx8fHw%3D&auto=format&fit=crop&w=400&q=60"]


async def fetch_data():
    print('Start Fetching the data')
    task = asyncio.create_task(show_progress())
    print('Going For Long....')
    await asyncio.sleep(20)
    print('Fetching Completed Result is Coming...')
    if task.done():
        print("Data We Get From Fetching is = ",task.result())



progress = 0
async def show_progress(progress):
    print(f"{progress} % Downloaded")
    await asyncio.sleep(0.2)

async def download_all(url,size):
    print("Start Downloading ...")
    for i in url:
        file_name = str(input("Enter the file name: "))
        task2 = asyncio.create_task(download_helper(i,file_name,size=0))
        await task2

async def util(file_name,response,type,size):
    print("Content-size  = ",size)
    global progress
    try:
        with open(f"{file_name}{type}",'wb') as file:
            for i in response.iter_content(chunk_size= 324 * 1024):
                file.write(i)

                if progress != 100:
                    await asyncio.create_task(show_progress(progress))
                    await asyncio.sleep(2)
                    progress  += 10
                path = os.path.abspath(file.name)
    except TypeError as e:
            print("Invalid Type")


async def download_helper(url,file_name,size):
    response = requests.get(url=url,stream=True)
    size = response.headers.get('Content-Length')
    print(size)
    size = int(size)
    if size != None:
        if(size >= 1024):
            size = (size / 1024) / 100
        else:
            size = size /  8
    else:
        size = 2
    path = None
    if(response.headers.get('Content-Type') == 'image/jpeg'):
        pass

    elif(response.headers.get('Content-Type')=='audio/mp4'):
        await util(file_name,response,'.mp3',size=size)

    elif(response.headers.get('Content-Type') == 'application/octet-stream'):
       await util(file_name,response,'.exe',size=size)

    return path

asyncio.run(download_all(["https://aac.saavncdn.com/438/93962c985186eb21ffe42ccada83db78_160.mp4"],0))


