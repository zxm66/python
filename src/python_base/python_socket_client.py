
import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('127.0.0.1',9090))
    data = s.recvfrom(1024)
    print(data)
    s.close()
    pass
