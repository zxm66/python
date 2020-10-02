# 装饰器做权限验证

user_permission = 7

# 权限因子
DEL_PERMISSION=8   # 1000 & 1011 ==> 1000
READ_PERMISSION=4  # 0100 & 1011 ==> 0000
WRITE_PERMISSION=2 # 0010 & 1011 ==> 0010
EXE_PERMISSION=1   # 0001 & 1011 ==> 0001

def check_permission(x,y):
    def handle_action(fn):
        def do_action():
            if x & y != 0:
                fn()
            else:
                print("当前用户没有权限")
        return do_action
    return handle_action

@check_permission(user_permission,READ_PERMISSION)
def read():
    print("this is read ")
    pass

@check_permission(user_permission,WRITE_PERMISSION)
def write():
    print("this is write ")
    pass

@check_permission(user_permission,EXE_PERMISSION)
def exe():
    print("this is exe ")
    pass

@check_permission(user_permission,DEL_PERMISSION)
def delete():
    print("this is delete ")
    pass

if __name__ == "__main__":
    read()
    write()
    exe()
    delete()
    pass
