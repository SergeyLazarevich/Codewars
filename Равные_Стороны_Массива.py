from random import randint


def find_even_index(lists: list)->int:
    index=-1
    for step in range(2,len(lists)):
        for i in range(step,len(lists)-step):
            if i<step and (sum(lists[:i])-sum(lists[i+1:i+(step+1)]))==0: 
                index=i
                break
            # elif i>(len(lists)-step-1) and sum(lists[i-step:i])-sum(lists[i+1:])==0:
            #     index=i
            #     break
            else:
                if sum(lists[i-step:i])-sum(lists[i+1:i+(step+1)])==0:
                    index=i
                    break
        if index>=0 or step>=len(lists)-1:
            print("step = ",step)
            break
    return index


# y=[randint(0,30) for i in range(20)]
# Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
# Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# Test.assert_equals(find_even_index(list(range(1,100))),-1)
# Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# Test.assert_equals(find_even_index(list(range(-100,-1))),-1)

print(find_even_index([17, 12, 0, 7, -4, 10, -1, 10, 32, 10, -1]))