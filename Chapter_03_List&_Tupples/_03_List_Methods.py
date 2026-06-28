# list methods 

"""
1)  list.append()               add elements in the end on the list 
2)  list.sort() and             ascending sort
    list.sort(reverse=True)     for desending sort the list 
3)  list.reverse()      reverse the whole list
4)  list.remove()       remove the first occurance or element
5)  list.pop(ind)       remove the index value 

"""


#1  FIRST --> append()
list = [2, 1, 3]
list.append(4)
print(list)
# ----------------------------------------------


# ASCENDING ORDER 
#2  SECOND -->  sort()  this function sort the list by assending order 
print(list.sort())
list.sort()
print("Assending order list is ",list)

# DISENDING ORDER 
# this method sort the list in descending order 
list.sort(reverse=True)
print("dissending order list is ",list)
# -----------------------------------------------------

#3 THIRD METHOD  reverse() method 
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
list1.reverse()
print(list1)
# ---------------------------------------------


#4 FOURTH METHOD insert(idx, val)
list.insert(2, 12)
print(list)
print("\n")
# -----------------------------------------------------


#5 FIFTH METHOD remove(val)  --> remove first occurence of element
val = [2, 1, 3, 1, 1]
val.remove(1)
print(val)

# pop method remove index val  method 
# pop(idx)
val.pop(3)
print(val)