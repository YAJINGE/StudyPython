list = ['www','baidu','com']
str = '.'.join(list)
str1 = '+'.join(list)
print(str)
print(str1)

tuple = ('xiajing','yajing')
str2 = '*'.join(tuple)
print(str2)

def sayhello():
    print('hello word')
sayhello()

def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(1,5))