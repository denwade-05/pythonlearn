'''
"""简单购物车,要求如下：
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，
购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
"""　　
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
'''
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
l=[]
while(True):
    name=input('商品名称：')
    if msg_dic.get(name)==None:
        continue
    else:
        count=input('购买个数：')
    l.append((name,msg_dic[name],count))
    print(l)