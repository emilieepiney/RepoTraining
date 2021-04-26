# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    """
    multiline comment
    """
    #single line comment

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print('i master python')
number=500
print(number,type(number))
number="whaat? does it work?"
print(number,type(number))
z=5j
print(z,type(z))
booleanv=True
strv="string"
print(0b111) #binary should have prefix 0b

empty_list=[]
list_str=["bmw","mercedes"]
mixed_list=['Nissan',1,True,2.5] # first element = 0 ; last element = -1
print(mixed_list[-1])
len(mixed_list)
print(mixed_list[1:3]) ##Attention : 3ème élémenet non compris
mixed_list[0]='Toyota'
mixed_list.append("coucou")
print(mixed_list)
mixed_list.insert(2,'nissan')
print(mixed_list)
mixed_list.extend([3,4])
print(mixed_list)
lst2=list_str+mixed_list
print(lst2.index(3))
lst2.remove(3)

a=2
a+=1
a*=10

lst2+=["a","b"]
print(lst2)
lst=[3,563,8,4]
lst.sort()
lst2.reverse()
lst.pop() # remove last element
lst.append(3)
print(lst.count(3))
set(lst)
lst3=lst.copy()
lst.clear()
print(lst3,lst)
del lst
#print(lst) ##Error

lst=lst3 ##shallow copy > changes from one list are seen in the other one !!


list_num=[20,70,80,60,40]
print(max(list_num),min(list_num),len(list_num))
list_num.sort()
list_num.append(25)
sorted_list_num=sorted(list_num) ## original object not changed
list_num*=2
## 0 = FALSE ; all other positive number = TRUE
print(all([0]))
print(all([0.2]))
print(all([0,0.2]))
print(all([list_num]))

print(any([0]))
print(any([0.2]))
print(any([0,0.2]))
print(any([list_num]))
new_num_list=[]
print(any(new_num_list)) ##FALSE
print(all(new_num_list)) ##TRUE

import numpy as np

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
