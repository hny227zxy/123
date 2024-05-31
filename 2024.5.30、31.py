'''30号函数的嵌套'''
def fun1(x,y):
    print("这是函数一")
    sum = x + y
    return  sum

def fun2():
    print("这是函数二")
    sum = fun1(x = 2,y = 3)
    print(sum)
fun2()

def max(x,y):
    return x if x > y else y

def maxs(a,b,c,d):
    res1 = max(a,b);
    res2 = max(res1,c);
    res3 = max(res2,d);
    return  res3;
print(maxs(5,2,420,299));

'''递归'''
def factorial(n):
    if n == 1:
        return  1
    r = n*factorial(n-1)#递归函数
    return  r
#测试
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
#猴子吃桃
n = int(input())#输入任意n表示第n天，剩下一个桃子
def F(x):
    if x == 1:
        return x#边界
    else:
        return (F(x-1)+1)*2#递归函数
print(F(n))#输出递归值



#31日
#date类
from datetime import datetime

a = datetime.today()
print(a)
print(a.year)  #输出年
print(a.month) #输出月
print(a.day)   #输出日


from datetime import date

a=date.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
a=date(2017,3,15)
b=date(2017,3,15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))
print(a.__sub__(b))
print(a.__rsub__(b))




#time类
from datetime import time
a=time(12,20,30,899)

print(a)
print(a.__format__('%H:%M:%S'))



from datetime import  *
d=date(2012,12,12)
print(d)

#昨天
d1=d+timedelta(days=-1)
print(d1)
#明天
d2=d+timedelta(days=1)
print(d2)
#上一个小时
dt3=dt+timedelta(hours=-1)
print(dt3)
#下一个小时
dt4=dt+timedelta(hours=1)
print(dt4)