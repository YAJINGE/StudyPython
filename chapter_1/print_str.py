name = '夏晶'
age = 28
money = 8720.578
print('欢迎'+name+'的到来,今年你',age,'岁哟!目前资产',money,sep='')
print('欢迎%s的到来,今年你%d岁哟!目前资产%.2f' %(name,age,money))
print('欢迎{name}的到来,今年你{age}岁哟!目前资产{m:.2f}'.format(name=name,age=age,m=money))
# f_string格式输出
print(f'欢迎{name}的到来,今年你{age}岁哟!目前资产{money:.2f}')