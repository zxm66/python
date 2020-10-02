

# exception keyword
# 自定义异常
# 系统内置的异常 ZeroDivisionError FileNotFoundError FileExistsError ValueError KeyError SyntaxError  
# 


class CustomException(Exception):
    
    def __init__(self) -> None:
        pass
    
    pass


def keyword_test():
    try:
        x = div(1,0)
    except Exception as e:
        print("this code exception is {}".format(e))
        # 抛出异常
        try:
            raise e
        except Exception:
            print("this is raise e")
        finally:
            print("this is finally")
    else:
        print("this code has not exception")
    finally:
        print("this code at finally")
    pass


def div(a,b):
    return a / b
if __name__ == "__main__":

    try:
        raise CustomException()
    except CustomException as e:
        print("this class is {}".format(e.__class__))
    pass
