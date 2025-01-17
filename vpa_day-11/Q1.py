# Write a program with two threads:
#   - One simulates downloading a file.
#   - The other updates a progress bar.

import threading
import time

download_complete = False

def download():
    global download_complete
    for i in range(1,101):
        time.sleep(0.1)
        progress = i
        print(f"Download is {progress}")
    download_complete = True
    
def update():
    while not download_complete:
        for i in range(1, 101):
            if download_complete:
                break
            print(f"Progress: [{'#' * i}{'.' * (100 - i)}] {i}%")
            time.sleep(0.1)
    
download_thread = threading.Thread(target=download)
progess_thread = threading.Thread(target=update)

download_thread.start()
progess_thread.start()

download_thread.join()
progess_thread.join()   