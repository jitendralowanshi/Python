"""
1)  str.endsWith()
2)  str.capatilize()
3)  str.replace("old", "new")
4)  str.find()
5)  str.count()

"""

str = "i am a coder ,am am am "

# 1 FIRST FUNCTION
print(str.endswith("er")) #this is first funtion 


# 2 SECOND FUNCTION
# str = str.capitalize()  # Some changes IN  original strings.
print(str.capitalize())


# 3 THIRD  FUNCTION 
print(str.replace("i", "A"))
print(str.replace("c", "B"))
print(str.replace("coder","jitendra"))


# 4 FOURTH FUNCTION 
print(str.find("coder"))   #this retun , coder start index retur 

# 5 FIFTH FUNCTION
str.count("am")
print(str.count("am"))   #this function count word exist in our variable
print("\n")



#=============================================

# first practice quetion
name = input("Enter Your first name ")

# length = len(name)
print("your length is : ",len(name))