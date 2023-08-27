import logging
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import time
class DummyDatabases:
    def __init__(self) -> None:
        self.value = 0
        self._lock = Lock()

    def update(self,name):
        logging.info("Thread : %s starting update",name)
        if self._lock.locked:
            logging.debug("Thread is locked %s",name)

        with self._lock:
            local_copy = self.value
            local_copy = local_copy + 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release the lock",name)
            logging.debug("Value is %d",self.value)
        
        logging.debug("thread %s after release",name)
        logging.info("thread : %s finished",name)


if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format,level=logging.DEBUG,datefmt="%H:%M:%S")
    db = DummyDatabases()
    with ThreadPoolExecutor(max_workers=8) as executor:
        for index in range(8):
            executor.submit(db.update,index)

    logging.info("Testing update. Ending Value is %d",db.value)
