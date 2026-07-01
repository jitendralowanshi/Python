"""
while loops 
for val in nums :



"""

"""
val = 1
while val <= 10 :
    print("Hello world", val)
    val += 1

    val1 = 10
    while val >= 1 :
        print("hello")
        val -= 1

"""

n = int(input("Enter your number :"))
i = 1
while i <= 10 :
    print(i*n)
    i += 1

print("loop indeds")


num = 1
while num <= 10 :
    if(num == 5) :
        break
    print(num)
    num += 1

# -----------------------------------------------------------------------

for val in range(10):
    print("jitendra lowanshi")


str = "jitendralowanshi"
for char in str :
    print(char)

# -----------------------------------------------------

"""
range()

range function returns a sequence of numbers, starting from 0 by default , and increments by 1 by default 
and stop before a specified number

range(start?, stop, stepsize?)
"""

for el in range(5):
    print(el)
print("\n")


for el in range(1, 5):
    print(el)
print("\n")

for el in range(1, 5, 2):
    print(el)
print("\n")



nums = int(input("enter your numbes : "))
for mul in range(1, 11):
    print(mul*nums)


for i in range (100):
    pass

if i > 5 :
    pass

print("abc")