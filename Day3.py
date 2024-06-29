"""
list = mutable  []
tple = imutable  ()

"""

# tpl = (10,20,30,40,'upfalirs',True)
# print(tpl)
# print(type(tpl))
# print(tpl[2:6])           # accessing iteam
# tpl[2] = 'Don'           # changing does not allow
# del tpl[2]
# print(tpl)

# imutable not allow
# tuple accessing  allow
# deletion and insertion not allow

####>>>>>>>>>>>>>>>>  SET   >>>>>>>>>>>>>>>>>>#########
# multiple, different types of iteam store
# duplicate  are not allow
# unorder collection of data item

# imutable
# tuple accessing not allow
# deletion is also allow
#insertion is allow

# remove and discard are allow to remove item in the set
#remove raise error in remove item in set
# discard are not raise error in remove the item in set

# set = {10,20,30,40,50,74,"upfalirs",True,90,80,70,10,10,10,10,10,101,10,10}
# print(set)
# print(type(set))

# st = {11,88,66,99,63,47,74,65,78,98}
# # st.add(1000)
# # st.remove(88)
# st.discard(11)
# print(st)


# st1 = {11,22,33,44,55,66,77,88,99}
# st2 = {11,88,23,1000,2000}

# st1.update(st2)
# print(st1)

# st ={2,3,34,56,56,56,56,7}
# st2={2,3,34,555,888,999,666}
# st.update(st2) 
# st.intersection(st2)

# print(st.intersection(st2))

# ls = [25,41,63,96,85,74,852]
# ls2 = ls 
# ls2[2] = 'upflairs'
# print(ls)
# print(ls2)

# ls2 = ls.copy()
# ls2[2] = "upflairs"
# print(ls2)
# print(ls)


###>>>>>>>>>>>>>>>>  Dictionary   >>>>>>>>##############

# mutable
#manipulation
# insertion
# update fuction are combine two set in dictionary

# dt = {'a':10,'b':20,'c':30,'d':40,5:6,'elephant':60}
# print(dt)
# print(type(dt))

# dt = {'A':10,'B':20,'C':30,'D':40,'E':50}
# print(dt['C'])
# print(dt.keys())
# print(dt.values())

# dt.pop('C')
# print(dt)

# dt['F'] = 700
# dt['G'] = 400
# print(dt)


# dt1 = {'A':10,'B':20,'C':30,'D':40,'E':50}
# dt2 = {'F':60,'G':70,'H':80,'I':90,'J':500}
# dt1.update(dt2)
# print(dt1)

student = {"Name":["Mohit","Rohit","kallu","Ruchi","Shalu"],
           "Marks":[80,87,90,98,56],
           "Subject":"physics"}
# print(student)
# print(type(student))

# student['sbject']='chemistry'
# print(student)

# student['Name'] = 'Raju'
# student['Marks'] = 25
# print(student)
# insert record
# 1. name = Raju
# Marks = 25
# last position in this list

n_name = "Raju"
n_marks = 25
student["Name"].append(n_name)
student["Marks"].append(n_marks)
print(student)



# 2. name = Raju
# Marks = 25
# first 1st position in this list

# student["Name"].insert(0, "Raju")
# student["Marks"].insert(0, 25)
# print(student)

# kaluu = bhura replace

# student["Name"][2] = "bhura"
# print(student)


