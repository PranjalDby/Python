from concurrent.futures import ThreadPoolExecutor
import random
import threading
import requests
import time
download_list = [
    "https://w0.peakpx.com/wallpaper/600/322/HD-wallpaper-anime-boy-anime-boy-anime-boys-cute-cute-anime-boy-cute-anime-boys-lonely-sad-anime-boy-sad-anime-boys-thumbnail.jpg",
    "https://w0.peakpx.com/wallpaper/560/1001/HD-wallpaper-anime-boy-anime-anime-boy-anime-boys-demon-depressed-lonely-sad-sad-anime-boy-sad-anime-boys-thumbnail.jpg",
    "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe"
    ]

music_list = ["https://aac.saavncdn.com/634/e808fd69b07dd312c532e76e774645e0_160.mp4", "https://aac.saavncdn.com/014/5a1c76a6977a2aab6e5bfcc1adbe029f_160.mp4",
              "https://aac.saavncdn.com/981/ff704210de1a556e6d59fe7241f94983_160.mp4"]


def download(url, filename):
    response = requests.get(url=url, stream=True)
    length = int(response.headers.get('Content-Length'))
    print(length)
    if (response.headers.get('Content-Type') == 'image/jpeg'):
        download_helper(response,filename,'jpeg',length)
    elif (response.headers.get('Content-Type') == 'audio/mp4'):
        download_helper(response,filename,'mp4',length)
    else:
        download_helper(response,filename,'exe',length)


def download_helper(response,file_name,type,length):
    try:
        with open(f"{file_name}.{type}", 'wb') as file:
            for i in response.iter_content(chunk_size=100 * 1024):
                dowloaded = (len(i)/length) * 100
                print("Downloading {} completed".format(dowloaded))
                file.write(i)
                time.sleep(0.2)
    except Exception as e:
        print("error")

    else:
        return True
    
    return False
    


if __name__ == '__main__':
    print("QAt maia")
    with ThreadPoolExecutor(max_workers=3) as e:
            for i in ["https://r4.wallpaperflare.com/wallpaper/67/241/223/assassin-s-creed-valhalla-video-games-video-game-art-digital-art-viking-hd-wallpaper-8f5a0d9d42d68da3237cfa4ecbf0452e.jpg"]:
                filename = str(input(f"Enter the file name for {i} = \n"))
                e.submit(download,i,filename)
                time.sleep(1)
