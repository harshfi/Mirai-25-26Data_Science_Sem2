
def func(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


func(1,2,3,4,5,6,7,8,9,10,name="John",age=30)