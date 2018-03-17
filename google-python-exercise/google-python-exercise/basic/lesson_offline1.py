"""特殊用法
if(18<age<40)
text='男'， if gender =='male' else '女'
slice切片
"""


"""列表推导式
生成器表达式"""
print(type(i**2 for i in range(100)))



"""dic"""
temp_dic={'dog':3,'spider':4}
temp_dic.get('cat',1)
temp_dic['dog']
temp_dic.setdefault('cat',5)
print(temp_dic)


"""eval"""
def test_first():
    return 2
def test_second(x):
    return x
tem_dic = {'param':5,'test_first':test_first,'test_second':test_second}

condition = 'param==5 and test_second(test_first)<3'
eval(condition,tem_dic)

"""zip"""
x=[1,2,3,4]
y=[5,6,7]
z=[8,9,0]
resault=list(zip(x,y,z))
print(resault)

new_resault=list(zip(*resault))
print(new_resault)


"""reduce"""
from functools import reduce 
print(reduce(lambda i,j:i+j,x))


"""list
map,reduce,filter,sorted,lambda
"""
tmplist = [1,3,4,6,7,8]
new_list=[x**2 for x in tmplist if x%3 == 0]
print(new_list)


def add100(x):
    return x+100

hh=[1,2,3]
new_hh=map(add100,hh)
print(new_hh)

mylist=['aaa','cc','BB','DD']
"""sorted(mylist,key=str.lower())

"""
"""
map(lambda x:x**2 if x%3==0 else x, templist)

"""