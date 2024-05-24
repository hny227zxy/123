def test_func(sum_num):
    #定义函数

    result = sum_num(range(1, 101))#调用 sum_num 函数（实际上是 dy 函数），将 range(1, 101) 作为参数传入，并将返回的结果（即 5050）存储在变量 result 中。
    print(result)#输出结果
dy = lambda x: sum(x)#简化函数，为函数命名。
test_func(dy)#调用函数，输出结果。
