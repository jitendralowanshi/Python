# Dictionary methods
"""
student.keys()      returns all keys
student.values()    return all values
student.item()      eturns all (key, value) pair as tupple
student.get("key")  return the key according to value
student.update(newDict)     returns the specified items to the dictionary

"""


info ={
    "name" : "jitendra",
    "surname" : "lowanshi",
    "email" : "jitendralowasnhi@gmail.com",
    "Dob" : "dd/mm/yyyy",
    "place" : "Hsrsud",
    "age" : "25",
    "gender" : "male"
}

# dictionary are unorderd

print(info)
print(type(info))

print(info["name"])
print(info["Dob"])

info["name"] = "sidharth"
print(info)

# add new key value pair
info["Mob"] = "1234567890"
print(info)
print("\n")

# ------------------------------------------------------------

student= {
    "name" : "jitndra lowanshi",
    "subjects" : {
        "dsa": 97,
        "os" : 90,
        "dbms" : 99,
        "cn" : 98
    }

}

# nested dictionary

print(student["subjects"]["dbms"])
print("\n")


# Dictionary methods 
print(info.keys())      #returns the keys 
print(info.values())    #return the values
print(info.items())     #return the key value pair in the form of tupple 
print(info.get("name")) #get any value using key 
print(info.get("email"))
print("\n")


newDict = {"city": "Indore", "course": "BE"}
info.update(newDict)
print(info)
print("\n")

print(list(info.items()))
print(len(info))