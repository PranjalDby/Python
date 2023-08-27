import requests
import multiprocessing
import time
#  multi-processing takes full advantage of cpu

session = None

def set_global_session():
    global session

    if not session:
        session = requests.Session()


def downlaod_site(url):
    with session.get(url) as resp:
        name = multiprocessing.current_process()
        print(f"{name}:Read {len(resp.content)}")

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(downlaod_site,sites)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
