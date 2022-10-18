# list, touple and range => sequencing 
# mapping dict
# set types set and frozen set

# list
# List items are ordered, changeable, and allow duplicate values.
# ordered => it means that the items have a defined order, and that order will not change.
# Changeable => means that we can change, add, and remove items in a list after it has been created.

thisList = ["apple", "banana", "cherry", "apple", "cherry"]

#Add list items
# Append Items

thisList.append("orange")

print("appended::", thisList)

# Insert Items 
# The insert() method inserts an item at the specified index:

newList = ["apple", "banana", "cherry"]
newList.insert(1,"orange")
print("insert::",newList)

#Extend List
# To append elements from another list to the current list, use the extend() method.
aList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

aList.extend(tropical)

print("extended::", aList)

# Add any iterable 
# The extend() method does not have to append list, you can add any
# Iterable object(tuples, sets, dictionaris etc.).

thisaList = ["apple", "banana", "cherry"]
thisaTuple = ("kiwi", "orange")

thisaList.extend(thisaTuple)

print("extended a iterable::", thisaList)

# Remove Specified Item
# The remove() method removes the specified Item,

List1 = ["apple", "banana", "cherry"]
List1.remove("banana")
print("List1::", List1)

# pop()
# The pop() method removes the specified index.

List2 = ["apple", "banana", "cherry"]
List2.pop(0)

print("List2", List2)

# If you do not specify the index, the pop() method removes the last item

list3= ["man", "female", "dog"]
list3.pop()
print("list3::", list3)

# The del keyword also removes the specified index

delList = ["apple", "mango", "cherry"]
del delList[0]
print("delList", delList)

# The del keyword can also delete the list completely.
newdelList =["apple", "banana", "cherry"]
del newdelList

# The clear() method empties the list. The list still remains, but it has no content.
clearList = ["apple", "banana", "cherry"]
clearList.clear()
print("clear", clearList)