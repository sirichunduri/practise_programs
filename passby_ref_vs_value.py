#pass by reference

def updatelist(list1):
    list1 +=[10]
n=[5,6]
'''
print(id(n))
updatelist(n)
print(id(n))
print(n)
'''

#pass by value
def updatenum(s):
    print(id(s))
    s+=10
    print("s is",s)

b=5
''' 
print(id(b))
updatenum(b)
print(id(b))
print(b) '''





'''Python is “pass-by-object-reference” “Object references are passed by value.”'''


# pass by value in list creates a copy there by does'nt change the original list as below

def reassign(list1):
    list1=[0,1]
    print(list1)

list1=[0]
reassign(list1)
print("last",list1)