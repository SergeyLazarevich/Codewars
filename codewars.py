
# def order(sentence):
#     return ' '.join(sorted(sentence.split(), key=lambda w:sorted(w)))

# test_1 = 'is2 Thi1s T4est 3a' # "Thi1s is2 3a T4est"
# test_2 = '4of Fo1r pe6ople g3ood th5e the2' # "Fo1r the2 g3ood 4of th5e pe6ople"
# test_3 = '' # ""

# test_1 = [ 1, 1, 1, 2, 1, 1 ] # "Thi1s is2 3a T4est"
# test_2 = [ 0, 0, 0.55, 0, 0 ] # "Fo1r the2 g3ood 4of th5e pe6ople"
# test_3 = [ 3, 10, 3, 3, 3 ]

# def find_uniq(arr):
#     arr = sorted(arr)
#     if arr[0] != arr[len(arr)//2]:
#         return arr[0] 
#     else:
#         return arr[-1]

# Completed in 163.52ms
# Completed in 176.56ms
# print(find_uniq(test_1))
# print(find_uniq(test_2))
# print(find_uniq(test_3))

# test_1 = "hello"#["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# test_2 = "codewars"# ["Codewars", "cOdewars", "coDewars", "codEwars", "codeWars", "codewArs", "codewaRs", "codewarS"]
# test_3 = "two words"#["Two words", "tWo words", "twO words", "two Words", "two wOrds", "two woRds", "two worDs", "two wordS"]
# test_4 = " gap "#[" Gap ", " gAp ", " gaP "]


# def wave(people):
#     lst = []
#     i = 0
#     for n in people:
#         if n != " ":
#             lst.append(f"{people[:i]}{n.upper()}{people[i+1:]}")
#         i +=1
#     return lst
#     # return [f"{people[:i]}{people[i].upper()}{people[i+1:]}" for i in range(len(people)) if people[i] != " "]

# Completed in 76.39ms
# Completed in 72.97ms
# print(wave(test_1))
# print(wave(test_2))
# print(wave(test_3))
# print(wave(test_4))


# test_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]#  "(123) 456-7890"
# test_2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]# "(111) 111-1111"
# test_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]# "(123) 456-7890"
# test_4 = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]# "(023) 056-0890"

# def create_phone_number(n):
#     n = "".join(list(map(str, n)))
#     return f'({n[:3]}) {n[3:6]}-{n[6:]}'

# print(create_phone_number(test_1))
# print(create_phone_number(test_2))
# print(create_phone_number(test_3))
# print(create_phone_number(test_4))

# test_1 = 0# 0
# test_2 = 4# 1
# test_3 = 7# 3
# test_4 = 9# 2

# def count_bits(n):
#     return f"{n:b}".count("1")

# print(count_bits(test_1))
# print(count_bits(test_2))
# print(count_bits(test_3))
# print(count_bits(test_4))


# [1]-1 ()
# [1][2]-3 (2+1)-2
# [1][2][3]-6 (3+2+1)-3
# [1][2][3][4]-10 (4+3+2+1)-4  

# [1][2][3][4][5]-15 (5+4+3+2+1)-5 

# [1][2][3][4][5][6]-21 (6+5+4+3+2+1)-6

# [1][2][3][4][5][6][7]-28 (7+6+5+4+3+2+1)-7

# [1][2]
# [1][2] - 9 (2*3+2+1)

# [1][2][3]
# [1][2][3] - 18 (2*6+3+2+1)

# [1][2][3]
# [1][2][3]
# [1][2][3] - 34 (3*6+6+3+4+2+1 )

# [1][2][3]
# [1][2][3]
# [1][2][3]
# [1][2][3] - 51 (4*6+9+6+9+2+1)


# def number_of_rectangles(m = 1, n = 1):
#     n_m = n*m
#     sum = {i:0  for i in range(1,n_m + 1)} 
#     for i in range(1,n_m+1):
#         if i == 1:
#             sum[i] = n_m
#         else:
#             for j in range(n_m,i,-i):
#                 if (j // i) > 0:
#                     sum[i] = sum[i] + (j // i)
#     return sum

# print(number_of_rectangles(3,3))
#print(number_of_rectangles(2,3))
#print(number_of_rectangles(2,7))


# def tour(friends, friend_towns, home_to_town_distances):
#     if len(friends) == 0: return 0
#     distances = []
#     friend_towns_ = {}
#     friend_towns_.update(friend_towns)
#     for i in range(len(friends)):
#         if friends[i] in friend_towns_.keys():
#             distances.append(friend_towns_[friends[i]])
#     way = home_to_town_distances[distances[0]]+home_to_town_distances[distances[-1]]
#     for i in range(1,len(distances)):
#         way += (home_to_town_distances[distances[i]]**2 - home_to_town_distances[distances[i-1]]**2)**0.5
#     return int(way)

# friends1 = ["A1", "A2", "A3", "A4", "A5"]
# fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
# distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
# # # 889
# print(tour(friends1,fTowns1,distTable1))
# print(list(distTable1.keys())[-1])




# try:
#     with open(r"Проекты Python\a.csv",'r',encoding="UTF-8") as obj_f:
#         with open(r"Проекты Python\a_1.txt",'w',encoding="UTF-8") as obj_f_a_1:
#             stroka=None
#             # slova=0
#             for stroka in obj_f:
#                 stroka = f"{stroka[:20]}{stroka[20:45].replace('.', ',')}{stroka[45:65]}{stroka[65:-1].replace('.', ',')}"
#                 print(stroka,file=obj_f_a_1)   
#                 # if slova>10:break
#                 # slova +=1
# except IOError as err:
#     print(err)
#
def lccm(a,b): 
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)

def convert_fracts(lst):
    if len(lst):
        mx = lst[0][1]
        for i in range(1,len(lst)):
            mx = lccm(mx,lst[i][1])
        for i in range(len(lst)):
            lst[i][0] = lst[i][0] * (mx //lst[i][1]) 
            lst[i][1] = mx
    return lst

#print(lccm(4, 6))
print(convert_fracts([[1, 6], [1, 4], [1, 8]]))
print(convert_fracts([[1, 6], [1, 4]]))
print(convert_fracts([[1, 6]]))
print(convert_fracts([]))



