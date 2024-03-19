# Dictionary {} =>
# Do not allow Duplicate,Duplicate value will overwrite existing  value
# Any type of data can be stored 
# key:value pair{"name":"EMC"}
# get(),key(),values(),items(),update({"year": 2023}),thisdict["color"]
# ="red",thisdict.pop("model"),del,clear()
a={ 
    "name":"EMC",
    "Age": 1,
    "address":'salem'
    }
a["color"]="red"
print(a.keys)

b={ 
    "name":"EMC",
    "Age": 1,
    "address":'salem'
    }
print(b.values())

c={ 
    "name":"EMC",
    "Age": 1,
    "address":'salem'
    }
c.update({"age":2})
print(c)

d={ 
    "name":"EMC",
    "Age": 1,
    "address":'salem'
    }
d.pop("Age")
print(d)