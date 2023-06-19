# QA COURSE

# TUPLES
#CODE1: Create an empty TUPLE
tup1 = ()
print("CODE1:")
# print the tuple list
print(f"tup1 = {tup1}")
# print the data type
print(f"data type = {type(tup1)}")
# print the length of the tuple
print(f"length = {len(tup1)}")
print()

#CODE2: Create TUPLE with 1 item
tup2 = ("cloudacademy",)
print("CODE2:")
print(f"tup2 = {tup2}")
print(f"data type = {type(tup2)}")
print(f"length = {len(tup2)}")
print()

#CODE3: Create TUPLE with multiple items of the same type
tup3 = (1, 2, 3, 4, 5)
print("CODE3:")
print(f"tup3 = {tup3}")
print(f"data type = {type(tup3)}")
print(f"length = {len(tup3)}")
print()

#CODE4: Create TUPLE with multiple items of different types
tup4 = ("cloud", "academy", 1, True, False)
print("CODE4:")
print(f"tup4 = {tup4}")
print(f"data type = {type(tup4)}")
print(f"length = {len(tup4)}")
print()

#CODE5: Iterate over TUPLE with multiple items
print("CODE5:")
# will print each item from the list on a separate line
for item in tup4:
  print(item)
print()

#CODE6: Search in TUPLE
print("CODE6:")
# boolean
print ("cloud" in tup4)
print ("blah" in tup4)
print()

#CODE7: Retrieve item from TUPLE
print("CODE7:")
# retrieve an item from the relevant index
item0 = tup4[0]
item1 = tup4[1]
print(f"item0 = {item0}")
print(f"item1 = {item1}")
print()

#CODE8: Attempt to change immutable TUPLE
print("CODE8:")
try:
  tup4[0] = "not possible!"
except:
  print("Tuples are immutable!!")
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# QA COURSE

# LISTS

#CODE1: Create an empty LIST
list1 = []
print("CODE1:")
print(f"list1 = {list1}")
print(f"data type = {type(list1)}")
print(f"length = {len(list1)}")
print()

#CODE2: Create LIST with 1 item
list2 = ["cloudacademy"]
print("CODE2:")
print(f"list2 = {list2}")
print(f"data type = {type(list2)}")
print(f"length = {len(list2)}")
print()

#CODE3: Create LIST with multiple items of the same type
list3 = [1, 2, 3, 4, 5]
print("CODE3:")
print(f"list3 = {list3}")
print(f"data type = {type(list3)}")
print(f"length = {len(list3)}")
print()

#CODE4: Create LIST with multiple items of different types
list4 = ["cloud", "academy", 1, True, False]
print("CODE4:")
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
print()

#CODE5: Iterate over LIST with multiple items
print("CODE5:")
for item in list4:
  print(item)
print()

#CODE6: Search in LIST
print("CODE6:")
print ("cloud" in list4)
print ("blah" in list4)
print()

#CODE7: Retrieve item from LIST
print("CODE7:")
item0 = list4[0]
item1 = list4[1]
print(f"item0 = {item0}")
print(f"item1 = {item1}")
print()

#CODE8: Change mutable LIST
print("CODE8:")
# change a certain index
list4[0] = "possible!!"
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
print()

#CODE9: Append to LIST
print("CODE9:")
list4.append("new item")
print(f"list4 = {list4}")
print(f"data type = {type(list4)}")
print(f"length = {len(list4)}")
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# QA COURSE

# SETS

#CODE1: Create an empty SET
set1 = set()
print("CODE1:")
print(f"set1 = {set1}")
print(f"data type = {type(set1)}")
print(f"length = {len(set1)}")
print()

#CODE2: Create SET with 1 item
set2 = {"cloudacademy"}
print("CODE2:")
print(f"set2 = {set2}")
print(f"data type = {type(set2)}")
print(f"length = {len(set2)}")
print()

#CODE3: Create SET with multiple items of the same type
set3 = {1, 2, 3, 4, 5}
print("CODE3:")
print(f"set3 = {set3}")
print(f"data type = {type(set3)}")
print(f"length = {len(set3)}")
print()

#CODE4: Create SET with multiple items of different types
set4 = {"cloud", "academy", 1, True, False}
print("CODE4:")
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")
print()

#CODE5: Iterate over SET with multiple items
print("CODE5:")
for item in set4:
  print(item)
print()

#CODE6: Search in SET
print("CODE6:")
print ("cloud" in set4)
print ("blah" in set4)
print()

#CODE7: Attempt to retrieve item from SET
print("CODE7:")
try:
  item0 = set4[0]
  item1 = set4[1]
  print(f"item0 = {item0}")
  print(f"item1 = {item1}")
except:
  print("Sets do not support indexing!!")
print()

#CODE8: Add new unique item to SET
print("CODE8:")
set4.add("devops")
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")
print()

#CODE9: Add new non-unique item to SET
print("CODE9:")
set4.add("devops") # added prev
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")
print()

#CODE10: Remove item from SET
print("CODE10:")
set4.remove("cloud")
print(f"set4 = {set4}")
print(f"data type = {type(set4)}")
print(f"length = {len(set4)}")
print()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# QA COURSE

# DICTIONARIES

#CODE1: Create an empty DICTIONARY
dict1 = {}
print("CODE1:")
print(f"dict1 = {dict1}")
print(f"data type = {type(dict1)}")
print(f"length = {len(dict1)}")
print()

#CODE2: Create DICTIONARY with 1 key-value pair
dict2 = {"name": "cloudacademy"}
print("CODE2:")
print(f"dict2 = {dict2}")
print(f"data type = {type(dict2)}")
print(f"length = {len(dict2)}")
print()

#CODE3: Create DICTIONARY with multiple key-value pairs
dict3 = {"name": "cloudacademy", "color": "red", "count": 1000}
print("CODE3:")
print(f"dict3 = {dict3}")
print(f"data type = {type(dict3)}")
print(f"length = {len(dict3)}")
print()

#CODE4: Create DICTIONARY with multiple and nested key-value pairs
dict4 = {"name": "cloudacademy", "color": "red", "count": 1000, "data": {"val1": 1, "val2": 2}}
print("CODE4:")
print(f"set4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE5: Iterate over DICTIONARY with multiple and nested key-value pairs
print("CODE5:")
for key, value in dict4.items():
 print(f"key={key}, value={value}")
print()

#CODE6: Search key in DICTIONARY
print("CODE6:")
print ("name" in dict4)
print ("cloudacademy" in dict4)
print()

#CODE7: Retrieve value from DICTIONARY by key
print("CODE7:")
item0 = dict4["name"]
item1 = dict4["color"]
print(f"item0 = {item0}")
print(f"item1 = {item1}")
print()

#CODE8: Change existing value in DICTIONARY
print("CODE8:")
dict4["name"] = "blah"
dict4["color"] = "blue"
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE9: Add new key-value pair to DICTIONARY
print("CODE9:")
dict4['qwerty'] = 'fast'
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE10: Pop existing key-value pair from DICTIONARY
print("CODE10:")
test = dict4.pop('qwerty', None)
print(f"test = {test}")
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()

#CODE11: Pop non-existing key-value pair from DICTIONARY
print("CODE11:")
test = dict4.pop('cat', None)
print(f"test = {test}")
print(f"dict4 = {dict4}")
print(f"data type = {type(dict4)}")
print(f"length = {len(dict4)}")
print()
