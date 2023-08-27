import requests
import time
from concurrent.futures import ThreadPoolExecutor
import threading
thread_local = threading.local()
def get_own_sessions():

    if not hasattr(thread_local,"session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_own_sessions()
    with session.get(url) as response:
        print("inside with")
        # print(f"Readin {response.content}")
        pass

def download_helper(sites):
    with ThreadPoolExecutor(max_workers=10) as e:
        for i in range(10):
            e.map(download_site,sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ]

    start_time = time.time()
    download_helper(sites)
    # with ThreadPoolExecutor(max_workers=10) as e:
    #     for i in range(10):
    #         e.map(download_helper,sites)
    duration = time.time()-start_time
    print(f"downloaded in {duration} seconds")