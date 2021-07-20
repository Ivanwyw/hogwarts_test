#   闭包函数
#   返回值为嵌套的函数

##  1.理解闭包函数和闭包函数的调用
##  2.理解变量在函数的作用域

#name = "鲸鱼"
def func1():
    print(name)
    print("我是func1")
    def func2():
        name = "虾米"
        print(name)
        print("我是func2")
    # 返回的是一个函数   不是函数的调用
    return func2


func1()()
