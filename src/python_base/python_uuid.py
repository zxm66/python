
import uuid

if __name__ == "__main__":
    #print(str(uuid.uuid1()).replace('-',''))
    #基于mac地址
    print(uuid.uuid1())
    #md5
    print(uuid.uuid3(uuid.NAMESPACE_DNS,"zhangsan"))
    #sha
    print(uuid.uuid5(uuid.NAMESPACE_DNS,"zhangsan"))
    # 使用uuid4使用随机数。
    print(uuid.uuid4())
    pass
