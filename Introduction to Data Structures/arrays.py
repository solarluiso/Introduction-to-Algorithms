# Accessing Elements
new_list = [1, 2, 3, 4, 5]
result = new_list[0]

print(result)


if 4 in new_list: print(True)

for n in new_list:
  if n == 4:
    print(True)
    break


# List Length
numbers = [1, 2, 3, 4, 5, 6]
print(len(numbers))

for i in range(len(numbers)): # it is a good practice to iterate over a list with a range defined by the length of the list
  print(numbers[i])


# List Operations
numbers.append(7) # Adds 7 to the end of the list
numbers.extend([8, 9, 10]) # To add (or concatenate) one list to another
numbers.insert(10, 11) # Inserts 11 at index 10
numbers.remove(11) # Removes the first occurrence of 11

print(numbers)

print(numbers.index(4)) # Returns the index of the first occurrence of 4


# List Membership
if 5 in numbers: print(True) 
if 30 not in numbers: print(True)

numbers[0] = 22 # Updates first element in list to 22
print(numbers)