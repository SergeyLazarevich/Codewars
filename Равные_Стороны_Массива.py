from random import randint


def fun(lists: list)->int:
    index=-1
    for step in range(2,len(y)):
        for i in range(len(lists)):
            if i<step and (sum(lists[:i])-sum(lists[i+1:i+(step+1)]))==0: 
                index=i
                break
            elif i>(len(lists)-step-1) and sum(lists[i-step:i])-sum(lists[i+1:])==0:
                index=i
                break
            elif sum(lists[i-step:i])-sum(lists[i+1:i+(step+1)])==0:
                index=i
                break
        if index>=0:
            break
    return index


y=[randint(0,30) for i in range(20)]
print(fun(y))