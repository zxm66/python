
import socket
import threading

# 使用多线程编程。

def client():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',9090))
    data = s.recvfrom(1024)
    print(data)
    s.close()
    pass

def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',8080))
    s.sendto('good monring'.encode('utf8'),('127.0.0.1',9090))
    s.close()
    pass
if __name__ == "__main__":
    s = threading.Thread(target=server)
    c = threading.Thread(target=client)
    # s.start 写在上边是接收不到消息的，是应为server程序结束了吗？我想是的。
    c.start()
    s.start()
    pass
