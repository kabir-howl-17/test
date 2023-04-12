queue = list()

def enqueue(x):
    global queue
    queue.append(x)


def deque(x):
    global queue
    if isempty():
        return "queue is like your brain"
    x = queue.pop(0)
    return x

def isempty():
    global queue
    
    return len(queue)==0



enqueue(6)
enqueue(7)
enqueue(8)
print(isempty())
print(queue)