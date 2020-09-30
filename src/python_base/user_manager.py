users = [
        {"id":"1","name":"zhangsan"},
        {"id":"2","name":"lisi"},
        ]
def query_all():
    return users;

# filter 参数 函数 + 数据

def query_by_id(id):
    return filter(lambda a : a["id"] == id,users).__next__()

# 根据id修改list的元素
def update(user):

    pass

def delete(id):
    obj = filter(lambda a:a["id"] == id,users).__next__()
    return users.remove(obj)

def add(user):
    users.__add__(user)
    pass

if __name__ == "__main__":
    print("欢迎进入用户管理系统\n    1.查询所有用户信息\n    2.根据id查询用户信息\n    3.根据删除用户信息\n    4.增加一个用户\n    5.输入exit退出程序\n")

    while True:
        flag = input("请输入操作符号\n")
        if flag == "1":
            print(query_all())
        elif flag == "2":
            print(query_by_id(input("输入用户id\n")))
        elif flag == "3":
            print("")
        elif flag == "4":
            x = input("请输入一个用户信息")
            add(list([{"id":"3","name":"wangwu"}]))
            print(users)
        elif flag == "exit":
            exit(0)
