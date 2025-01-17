import threading
import multiprocessing
import time

def sum_of_squares_thread(n, result_list):
    result = sum(i * i for i in range(n))
    result_list.append(result)

def sum_of_squares_process(n, result_queue):
    result = sum(i * i for i in range(n))
    result_queue.put(result)

n = 10000000 

result_list = []
thread = threading.Thread(target=sum_of_squares_thread, args=(n, result_list))

start_thread = time.time()
thread.start()
thread.join()
end_thread = time.time()

print(f"Time for thread: {end_thread - start_thread} seconds")
print(f"Result (thread): {result_list[0]}")

# Using multiprocessing
result_queue = multiprocessing.Queue()
process = multiprocessing.Process(target=sum_of_squares_process, args=(n, result_queue))

start_process = time.time()
process.start()
process.join()
end_process = time.time()

print(f"Time for process: {end_process - start_process} seconds")
print(f"Result (process): {result_queue.get()}")
