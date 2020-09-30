
import hashlib
import hmac

# 这两个模块丢失用来进行数据加密
# hashlib模块里主要支持两种算法 md5 和 sha加密
# 加密方式：单项加密 md5/sha 对称加密 非对称加密 rsa
if __name__ == "__main__":
    x = hashlib.md5()
    x.update("abc".encode('utf8'))
    print(x.hexdigest())
    # 文件的md5,为了不让文件损坏。
    h1 = hashlib.sha1('123456'.encode())
    print(h1.hexdigest())
    h2 = hashlib.sha224('123456'.encode())
    print(h2.hexdigest())
    h3 = hashlib.sha256('123456'.encode())
    print(h3.hexdigest())
    h4 = hashlib.sha384('123456'.encode())
    print(h4.hexdigest())
    #  hmac 也是一种单向加密 可以指定密钥
    h = hmac.new('h'.encode(),"hello world".encode())
    print(h.hexdigest())
