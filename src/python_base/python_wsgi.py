from wsgiref.simple_server import make_server
import json

"""
    写框架是没有必要的，我要做的事情是数据在计算机是如何存在的。
    然后就是关于网络编程的各种网络协议是比较重要的。

"""
# environ 表示环境
# start_response 返回响应头
def demo_app(environ,start_response):
    path = environ['PATH_INFO']
    print('this path is {}'.format(path))
    response_header = ''
    response_body = ''

    if path == '/':
        response_body = 'welcome my web'
    elif path == '/login':
        response_body = 'welcome login'
    elif path == '/json':
        response_body = json.dumps({'name':'zhangxiaomin'})
    elif path == '/README.md':
        with open('README.md','r',encoding='utf8') as file:
            response_body = file.read()
    else:
        response_body ='页面不存在'
    response = response_header + response_body
    start_response('200 OK',[('Content-Type','text/html;charset=utf8')])
    return [response.encode('utf8')]
if __name__ == "__main__":
    httpd = make_server('',8080,demo_app)
    sa = httpd.socket.getsockname()
    print('this sa is {}'.format(sa))
    httpd.serve_forever()
    pass
