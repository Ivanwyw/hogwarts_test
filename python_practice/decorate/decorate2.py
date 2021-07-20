# 定义装饰器 形参 实参 是一个函数对象

def func1(func):
    func()
    def func2():
        #func()
        print("我是func2")

    return func2


# TypeError: func1() takes 0 positional arguments but 1 was given

@func1
def be_decorate():
    print("被装饰器装饰了的函数")


be_decorate()
#func1(be_decorate)()
