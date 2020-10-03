# http 协议
# hyperText Transfer Protocal 超文本传输协议
# 


import socket

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0',9090))
    # 128 排队的长度
    server_socket.listen(128)
    while True:
        client_socket ,client_addr = server_socket.accept()
        print(client_addr)
        data = client_socket.recv(1024).decode('utf8')
        if data:
            path = data.splitlines()[0].split(' ')[1]
            print("the path is {}".format(path))
            response_header = ''
            response_body= ''
            if path == '/':
                response_body= 'welcome my web'
            if path == '/login':
                response_body= 'welcome login page'
            if path == '/register':
                response_body= 'welcone register'
            response = response_header+response_body
            client_socket.send(response.encode('utf8'))
            print(data)
            pass
        else :
            pass
        if 1 == 2:
            break
        pass
    client_socket.close()
    server_socket.close()
    pass
