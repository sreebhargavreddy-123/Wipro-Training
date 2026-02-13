import requests
import threading
import time

urls = [
    "https://www.google.com",
    "https://www.yahoo.com",
    "https://www.rediff.com",
    "https://www.amazon.in"
]

# Function to download a URL and save it as data1.txt, data2.txt, etc.
def downloadfiles(url, index):
    try:
        response = requests.get(url)
        filename = f"data{index+1}.txt"  # data1.txt, data2.txt, ...
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# -------- Sequential Download --------
starttime = time.time()
for i, url in enumerate(urls):
    downloadfiles(url, i)
sequentialtime = time.time() - starttime
print(f"\nSequential download time: {sequentialtime:.2f} seconds")

# -------- Threaded Download --------
threads = []
starttime1 = time.time()

for i, url in enumerate(urls):
    thread = threading.Thread(target=downloadfiles, args=(url, i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

threadingtime = time.time() - starttime1
print(f"\nThreading download time: {threadingtime:.2f} seconds")
