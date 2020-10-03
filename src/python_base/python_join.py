import time
import threading


x = 10

def test(a,b):
    time.sleep(1)
    global x
    x = a + b
    pass

if __name__ == "__main__":
    t = threading.Thread(target=test,args=(1,1))
    #test(1,1)
    t.start()
    t.join()
    print(x)

    pass
