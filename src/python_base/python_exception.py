

# exception keyword


def div(a,b):
    return a / b
if __name__ == "__main__":
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
