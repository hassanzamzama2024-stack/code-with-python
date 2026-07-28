
fruits = ["apple", "mango", "banana", "orange", "grapes"]
print("List:", fruits)




print("First:", fruits[0]) 
print("Last:", fruits[-1]) 


print("Total:", len(fruits)) 


fruits.append("peach") 
print("After add:", fruits)


fruits.insert(1, "kiwi")
print("After insert:", fruits)


fruits.remove("banana") 
print("After remove:", fruits)


fruits.sort() 
print("After sort:", fruits)


fruits.reverse() 
print("After reverse:", fruits)


print("Final list:", fruits)