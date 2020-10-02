# 装饰器 是可以传递的。
def can_play(fn):
    print("this is can_play")
    def inner(name,game,**kwargs):
        fn(name,game)
        pass
    return inner
#@can_play
def say_hello(fn,num):
    print("say hello,this fn is {}".format(fn))
    return play_game_3
def say_bye(num):
    print("this num is {}".format(num))
    return play_game_2
def say_hehe(hehe):
    print("this hehe is {}".format(hehe))
    return play_game_1
def play_game_1(name,game):
    print("this is play_game_1, and the name is {} and the game is {}".format(name,game))
    pass
def play_game_2(name,game):
    print("this is play_game_2, and the name is {} and the game is {}".format(name,game))
    pass

def play_game_3(fn):
    print(' this play_game_3 this fn is {} '.format(fn))
    pass
@say_hehe
@say_hello(2,2)
@say_bye
def play_game(name,game):
    print("{} is playing {}".format(name,game))
    pass
if __name__ == "__main__":
    play_game("zhangsan","baseball")
    print("this is decorator.................")
    say_hehe(say_hello(2,2)(say_bye(play_game)))("zhangsan",'baseball')
    pass















