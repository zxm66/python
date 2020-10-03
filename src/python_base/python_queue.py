


import multiprocessing

if __name__ == "__main__":
    q = multiprocessing.Queue(5)
    q.put('hello')
    q.put('world')
    q.put('yes')
    q.put('good')
    q.put('dw')
    print(q.full())
    q.put('you',block=True,timeout=5)
    q.put('are',block=False)
    q.put_nowait('how')

    pass
