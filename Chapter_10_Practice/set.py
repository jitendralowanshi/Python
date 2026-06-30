"""
Set is the collection of the unorderde items
Each elements in the set must be unique & immutable.
set is mutable but set ke items are immutable


set.add(el)         adds an element
set.remove(el)      remove the element an
set.clear()         empties the set
set.pop()           remove a random value 

set1.union(set2)    combine both set values & return new set
set1.intersection(set2)         combines common values & returns new 

"""

set1 = {1,2,3,4}
set2 = {1,2,2,5,"hello"}

print(set1)
print(set2)

union = set1.union(set2)
print("union : ",union)


# do sets ki common values 
intersection = set1.intersection(set2)    
print("intersection : ",intersection)



# Empty set syntex
null_set = set()

null_set.add(1)
null_set.add(3)
null_set.add(5)

# null_set.remove(1)
# null_set.clear()

null_set.pop()
print(null_set)


null_set.pop()
print(null_set)