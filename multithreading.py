import threading

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

# Create two threads that increment the counter
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final value of the counter
print("Counter:", counter)