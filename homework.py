# aa=""
# e =[]
# def sum_of_numbers (aa):
#     w=0
#     q=aa.split("_")
#     for i in range(len(q)):
#         e.append(int(q[i]))
#
#     for x in e:
#         if not (x%2==0):
#           w+=x
#
#         else:
#             continue
#     print("the sum of all add numbers = ",w)
#
# sum_of_numbers("3_71_8_16_20")


# list1=[]
# list2=[]
# list3=[]
# def  two_lists (list1,list2):
#     for x in list1:
#         for i in list2:
#             if x==i:
#                 list3.append(x)
#     print(list3)
#
# two_lists (["3",77,"78","ahmed"],["78","ahmed",77])

# aa=""
# e =[]
# def list_of_numbers (aa):
#     q = aa.split("_")
#     for i in range(len(q)):
#              e.append(int(q[i]))
#     for x in e :
#         if e.count(x) > 1:
#             e.remove(x)
#     print(e)
#
# list_of_numbers ("77_77_77_88_92")



# aa=""
# e =[]
#
# def difference_between_the_max_min(aa):
#     q = aa.split("_")
#     for i in range(len(q)):
#         e.append(int(q[i]))
#     e.sort()
#     m = e[len(e) - 1] - e[0]
#     print("the difference between the maximum and minimum :", m)
# difference_between_the_max_min("77_99_30_13_150")


# aa=""
# e =[]
#
# def smallest_largest (aa):
# #     m=0
#     q = aa.split("_")
#     for i in range(len(q)):
#         e.append(int(q[i]))
#     e.sort()
#     print("the smallest value : ",e[0])
#     print("the largest value : ",e[len(e)-1])
# smallest_largest ("77_99_30_13_150")









#
# students ={
#     1: {"std_ID":2002020,"std_name": 'Ali',"grade":95},
#     2: {"std_ID":222222,"std_name": 'saja',"grade":80},
#     3: {"std_ID":333333,"std_name": 'lana',"grade":85},
#     4: {"std_ID":4444444444,"std_name": 'maram',"grade":95},
# }
# for std_number,std_data in students.items():
#     print('-'*20)
#     print("student number",std_number,":")
#     for key in std_data :
#         print(key,":",std_data[key])




# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
#
# list1.extend(list2)
#
# print(list1)


# my_list = [12, 3, 2023]
# my_list.insert(2, 'GSG')
# print(my_list)


# list1 = [10,20,30,40]
# list2= [item + 10 for item in list1]
# print (f'list1 is : {list1}\nlist2 is: {list2}' )
# summation = sum(list2)
# maximum = max (list2)
# minimum = min (list2)
# print(f'summation of list1 is: {sum(list1)}')# using sum
# print(f'summation of list2 is: {summation}')
# print(f'maximum of list2 is: {maximum}')
# print(f'minimum of list2 is: {minimum}')


# my_tuple = (10 , 50)
# my_tuple1 = 10 , 50 ,'GSG',(40,30,35)
# print(my_tuple)
# print(my_tuple1)
# print(type(my_tuple))
# print(f'my_tuple(1): {my_tuple1[1]}')
# print(f'my_tuple(-2):{my_tuple1[-2]}')
# print(f'Length of my_tuple is:{len(my_tuple1)}')

# b = (1, 3, 7, 8, 2, 6, 5)
# print(min(b))
# print(max(b))
# print(sorted(b))


# myString = "GSG "
# myList = [10, 20]
# myTuple = ("A", "B")
# print(myString * 3)
# print(myList * 3)
# print(myTuple * 3)


# mySet= {"Test", "GSG", 100}
# print(mySet)
#
# mySet2= {"GSG", 2, 7.5, True, (1, 2, 3)}
# print(mySet2)
#
# mySet3= {1, 2, "GSG", "One", "GSG", 1}
# print(mySet3)

# b = {"One", "Two", "Three"}
# c = {"1", "2", "3"}
# x = {"B", "C"}
# print(b | c)
# print(b.union(c, x))

# d = {1, 2, 3, 4}
# d.add(5)
# d.add(6)
# print(d)

#
# i = {"A","88", True, 1, 2, 3, 4, 5}
# print(i.pop())

# a1 = {1, 2, 3}
# a2 = {1, "A", "B", 2}
# a1.update(['GSG', "2023"])
# a2.update(a1)
# print(a2)
# print(a1)


# user = {
# "username": "Ali",
# "password": 123456,
# "gmail": "Ali99@gmail.com"
# }
# print(user)
# print(user['username'])
# print(user.get("username"))
# print(user.keys())
# print(user.values())
# for i,v in user.items() :
#     print (v)

# students = {
# "One": {
# "name": "Ahmed"
# ,
# "GPA": "80%"
# },
# "Two": {
# "name": "Ali"
# ,
# "GPA": "70%"
# },
# "Three": {
# "name": "sary"
# ,
# "GPA": "90%"
# }}
# print(students)
# print(students['One'])
# print(students['Three']['name'])
# print(len(students))
# print(len(students["Two"]))
#
#
# user = {
# "name": "Ghydaa"
# }
# print(user)
# user.clear()
# print(user)
# print("=" * 50)



# member = {
# "name": "Ghydaa"
# }
# print(member)
# member["age"] = 24
# print(member)
# member.update({"country": "Gaza"})
# print(member)

x=5
y=2
r=x/y
print(r)



