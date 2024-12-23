import sys
import queue
import threading
import select

q = queue.Queue()
run = True

def read():
    while run:
        # Use select to wait for input
        if select.select([sys.stdin], [], [], 0.05)[0]:
            q.put(sys.stdin.read(1))

t = threading.Thread(target=read)
t.start()

while True:
    key = q.get()
    print(f"{key!r}")
    if key == "q":
        run = False
        break
t.join()