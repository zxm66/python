

# 装饰器


def can_play(clock):
    def handle_action(fn):
        def do_action(name,game):
            if clock < 22:
                fn(name,game)
            else:
                print("this so latter")
            pass
        return do_action
    return handle_action
 
# 装饰器的工作过程
# 1.执行can_play 2.返回handle_action 3.将play_name作为参数传递给handle_action执行。
@can_play(21)
def play_game(name,game):
    print("{} is playing {}".format(name,game))
    return


if __name__ == "__main__":
    play_game("zhangsan","baseball")
    pass
