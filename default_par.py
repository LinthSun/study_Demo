# 函数的定义相当于一次类型构造，默认值只在此时解析一次。程序结束才会被销毁
# 而函数调用时不会重新执行默认参数的构造。所以，如果使用了字典，列表这样的可变类型。
# 而又要在函数体内修改它，可能会出现意想不到的效果.


def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')




def testFunc(val, list=None):
    list=list or [] 
    list.append(val)
    return list

list4 = testFunc(10)
list5 = testFunc(123,['h'])
list6 = testFunc('a')

#this part about object trap

class A(object):
    def __init__(self, c): 
        self.x.append(c)  
    x = []                

a1 = A(1)
a2 = A(2)

print(a1.x)
print(a2.x)

class B(object):
    x=[]
    def __init__(self):
        print("end")
    
b =B()
print(b)
m=[]



#python函数的默认参数大坑
obj=[]
class demo_list:
    def __init__(self, l=[]):
        self.l = l

    def add(self, ele):
        self.l.append(ele)

def appender(ele):
    obj.append(demo_list())
    obj[ele].add(ele)
    #print(obj[ele].l) 

if __name__ == "__main__":
    for i in range(5):
        appender(i)
    for i in range(5):
            print(obj[i])
            print(obj[i].l)







