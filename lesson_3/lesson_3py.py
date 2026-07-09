# tasks for lesson 3 :
# LIST TASKS
# 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
# 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
# 3. **Max Element**: From a given list, determine the largest element.
# 4. **Min Element**: From a given list, determine the smallest element.
# 5. **Check Element**: Given a list and an element, check if the element is present in the list.
# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
# 7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.
# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.
# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
# 20. **Find Second Largest**: From a given list, find the second largest element.
# 21. **Find Second Smallest**: From a given list, find the second smallest element.
# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
# 24. **List Length**: Determine the number of elements in the list.
# 25. **Create a Copy**: Create a new list that is a copy of the original list.
# 26. **Get Middle Element**: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.
# 27. **Find Maximum of Sublist**: Given a list, find the maximum element of a specified sublist.
# 28. **Find Minimum of Sublist**: Given a list, find the minimum element of a specified sublist.
# 29. **Remove Element by Index**: Given a list and an index, remove the element at that index if it exists.
# 30. **Check if List is Sorted**: Determine if the list is sorted in ascending order and return a boolean.
# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
# 33. **Find All Indices**: Given a list and an element, find all the indices of that element in the list.
# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
# 38. **Check Palindrome**: Given a list, check if the list is a palindrome (reads the same forwards and backwards).
# 39. **Create Nested List**: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.
# 40. **Get Unique Elements in Order**: Given a list, create a new list that contains unique elements while maintaining the original order.

#Q1
toys = ["bear", "ball", "spidy", "hulk", "bear"]
print(toys.count("bear"))


#Q2
numbers = [1,4,6,8,9,11,15,34,57]
total = 0
for n in numbers:
    total += n
print(total)


#Q3
numbers = [1,4,6,8,9,11,15,34,57]
print(max(numbers))

#Q4
numbers = [1,4,6,8,9,11,15,34,57]
print(min(numbers))

#Q5
toys = ["bear", "ball", "spidy", "hulk", "bear"]
hero = "spidy"
if  hero in toys:
    print("Yep, spidy is definitely in this list of toys")
else:
    print("Unfortunately, spidy is not on this precious list of toys")

#Q6
game_heros = ['Isaac', 'Connor', 'Steve', 'Sans', 'Sonic']
if len(game_heros) == 0:
    first = None
else:
    first = game_heros[0]
print(first)

#Q7

if len(game_heros) == 0:
    last = None
else:
    last = game_heros[-1]
print(last)

#Q8
new_heros = game_heros[:3]
print(new_heros)

#Q9
reverse_heros = game_heros[::-1]
print(reverse_heros)

#Q10
sorted_heros = sorted(game_heros)
print(sorted_heros)

#Q11
my_list = [1, 2, 2, 3, 4, 4, 4, 5]

unique_list = list(set(my_list))

print(unique_list)


#Q12
game_heros = ['Isaac', 'Connor', 'Steve', 'Sans', 'Sonic']
index = 2
element = 'Gordon Freeman'
game_heros.insert(index, element)
print(game_heros)

#Q13
game_heros = ['Isaac', 'Connor', 'Steve', 'Sans', 'Sonic', 'Steve']
game_heros.index('Steve')

#Q14
game_heros = []
if len(game_heros) == 0:
    empty = True
else:
    empty = False
print(empty)


#Q15
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
count = 0
for int in integers:
    if int % 2 == 0:
        count += 1
    else:
        continue 
print(count)



#Q16
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
count = 0
for int in integers:
    if int % 2 != 0:
        count += 1
    else:
        continue 
print(count)


#Q17
game_heros = ['Isaac', 'Connor', 'Steve', 'Sans', 'Sonic', 'Steve']
series_characters = ['Saul Goodman', 'Walter White', 'Jesse Pinkman']
mix = game_heros + series_characters
print(mix)

#Q18
main_list = [1, 2, 3, 4, 5]
sub = [3, 4]

main_str = str(main_list)
sub_str = str(sub)[1:-1]
found = sub_str in main_str
print(found)



#Q19
series_characters = ['Saul Goodman', 'Walter White', 'Jesse Pinkman']
element = input("Enter an element to replace: ")
new_element = input("Enter the new element: ")
series_characters[series_characters.index(element)] = new_element
print(series_characters)

#Q20
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
sorted_integers = sorted(integers)
print(sorted_integers[-2])


#Q21
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
sorted_integers = sorted(integers)
print(sorted_integers[1])

#Q22
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
even = []
for n in integers:
    if n%2 == 0:
        even.append(n)
print(even)


#Q23
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
odd = []
for n in integers:
    if n%2 != 0:
        odd.append(n)
print(odd)

#Q24
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
print(len(integers))

#Q25
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
copy_integers = integers.copy()
print(copy_integers)

#Q26
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46, 78]
length = len(integers)
if length % 2 == 0:
    even = integers[length //2 - 1 : length //2 + 1]
    print(even)
else:
    middle = integers[length //2]
    print(middle)
 


#Q27
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
sub = integers[2:5]
print(max(sub))

#Q28
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
sub = integers[2:5]
print(min(sub))

#Q29
integers = [1, 5, 7, 8, 10, 16, 20, 21, 31, 38, 46]
index = 4
integers.pop(index)
print(integers)


#Q30
numbers = [5, 18, 78, 3, 8, 54, 49]
sorted_numbers = sorted(numbers)
if numbers == sorted_numbers:
    sort = True
else:
    sort = False
print(sort)

#Q31
numbers = [5, 18, 78, 3, 8, 54, 49]
num = 3
result = []
for n in numbers:
    for i in range(num):
        result.append(n)

print(result)



#Q32
game_heros = ['Isaac', 'Connor', 'Steve', 'Sans', 'Sonic', 'Steve']
series_characters = ['Saul Goodman', 'Walter White', 'Jesse Pinkman']
merged = game_heros + series_characters
print(sorted(merged))

#Q33
numbers = [5, 18, 5, 78, 3, 8, 54, 5, 49]
target = 5
indices = []
for i, item in enumerate(numbers):
    if item == target:
        indices.append(i)
print(indices)


#Q34
numbers = [5, 18, 5, 78, 3, 8, 54, 5, 49]
rotated_num = numbers[-1:] + numbers[:-1]
print(rotated_num)   

#Q35
list = []
for n in range(10):
    list.append(n)
print(list)



#Q36
numbers = [-5, 18, 5, -78, 3, 8, 54, -5, 49]
sum = 0
for n in numbers:
    if n > 0:
        sum += n
print(sum)
    

#Q37
numbers = [-5, 18, 5, -78, 3, 8, 54, -5, 49]
sum = 0
for n in numbers:
    if n < 0:
        sum += n
print(sum)
    

#Q38
palindrome_list = ['racecar', 'level', 'racecar']
if palindrome_list == palindrome_list[::-1]:
    print("The list is palindrome")
else:
    print("The list is not palindrome")
    

#Q39
numbers = [-5, 18, 5, -78, 3, 8, 54, -5, 49]
n = 3
new = []
for i in range(0, len(numbers), n):
    new.append(numbers[i:i + n])
print(new)


#Q40
numbers = [-5, 18, -5, -78, 3, 8, 54, -5, 49]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
    
print(unique)

# ### Tuple Tasks
#
# 1. **Count Occurrences**: Given a tuple and an element, find how many times the element appears in the tuple.
# 2. **Max Element**: From a given tuple, determine the largest element.
# 3. **Min Element**: From a given tuple, determine the smallest element.
# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
# 5. **First Element**: Access the first element of a tuple, considering what to return if the tuple is empty.
# 6. **Last Element**: Access the last element of a tuple, considering what to return if the tuple is empty.
# 7. **Tuple Length**: Determine the number of elements in the tuple.
# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
# 11. **Get All Indices of Element**: Given a tuple and an element, find all the indices of that element in the tuple.
# 12. **Find Second Largest**: From a given tuple, find the second largest element.
# 13. **Find Second Smallest**: From a given tuple, find the second smallest element.
# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
# 16. **Check if Tuple is Sorted**: Determine if the tuple is sorted in ascending order and return a boolean.
# 17. **Find Maximum of Subtuple**: Given a tuple, find the maximum element of a specified subtuple.
# 18. **Find Minimum of Subtuple**: Given a tuple, find the minimum element of a specified subtuple.
# 19. **Remove Element by Value**: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.
# 20. **Create Nested Tuple**: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.
# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
# 24. **Check Palindrome**: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).
# 25. **Get Unique Elements**: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.

#Q1
tuple12 = (1, 2, 2, 3, 4,4, 5)
element = 2
count = tuple12.count(element)
print(count)

#Q2
tuple11 = (1, 2, 2, 3, 4,4, 5)
print(max(tuple11))


#Q3
tuplev = (1, 2, 2, 3, 4,4, 5)
print(min(tuplev))

#Q4
tuplen = (1, 2, 2, 3, 4,4, 5)
element = 4
if element in tuplen:
    print(f"{element} is in the tuple")
else:
    print(f"{element} is not in the tuple")

#Q5
tupley = (1, 2, 2, 3, 4,4, 5)
if tupley == ():
    print("The tuple is empty")
else:
    print(tupley[0])

#Q6
if tuple2 == ():
    print("The tuple is empty")
else:
    print(tuple2[-1])


#Q7
tuplew = (1, 2, 2, 3, 4,4, 5)
print(len(tuplew))

#Q8
tuplel = (1, 2, 2, 3, 4,4, 5)
new_tuple = tuplel[:3]
print(new_tuple)

#Q9
tupleq = (1, 2, 2, 3, 4,4, 5)
tuple_1 = (6,7,3,6,9,0)
combined = tupleq + tuple_1
print(combined)

#Q10
tuplet = ()
if tuplet == ():
    print("The tuple is empty")
else: 
    print("The tuple isn't empty")
    

#Q11
tupler = (1, 2, 2, 3, 4,4, 5)
n = 4
indices = []
for i, value in enumerate(tupler):
    if value == n:
        indices.append(i)
    
print(indices)



#Q12
tuple_original = (1, 8, 2, 16, 2, 3, 4,4, 5)
sort_tuple = sorted(tuple_original)
print(sort_tuple[-2])

#Q13
tuple_original = (1, 8, 2, 16, 2, 3, 4,4, 5)
sort_tuple = sorted(tuple_original)
print(sort_tuple[1])


#Q14
t = (5, )
print(type(t))

#Q15
list2 = [1,3,4,7,11]
result = []
for n in list2:
    result.append(n)

tuple_result = tuple(result)
print(tuple_result)


#Q16
tuple4 = (1, 2, 3)
if tuple4 == tuple(sorted(tuple4)):
    ascend = True
else:
    ascend = False
print(ascend)

#Q17
tuple5 = (1, 2, 3)
print(max(tuple5))


#Q18
tuple6 = (1,2,3)
print(min(tuple6))

#Q19
tuple7 = (1,2,3, 2, 4, 2)
element = 2
resultie = []
removed = False
for item in tuple7:
    if item == element and removed == False:
        removed = True
    else:
        resultie.append(item)

resultie = tuple(resultie)
print(resultie) 

#Q20
tuple8 = (1,2,3, 2, 4, 2)
n = 2
new = []
for i in range(0, len(tuple8), n):
    new.append(tuple8[i:i+n])
new = tuple(new)
print(new)


#Q21
tuple9 = (1,2,3,4,7,12,15)
num = 3
result = []
for t in tuple9:
    for i in range(num):
        result.append(t)

result = tuple(result)
print(result)

#Q22
tuple9 = []
el = 10
for n in range(el):
    tuple9.append(n)
tuple9 = tuple(tuple9)
print(tuple9)

#Q23
tuple1 = (3,4,56,79,2)
reversed = tuple1[::-1]
print(reversed)

#Q24
palindrome_tuple = ('racecar', 'level', 'racecar')
if palindrome_tuple == palindrome_tuple[::-1]:
    print("The list is palindrome tuple")
else:
    print("The list is not palindrome")
    


#Q25
numbers = (-5, 18, -5, -78, 3, 8, 54, -5, 49)
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
unique = tuple(unique)
print(unique)


# ### Set Tasks
#
# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.
# 5. **Check Element**: Given a set and an element, check if the element exists in the set.
# 6. **Set Length**: Determine the number of unique elements in a set.
# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
# 8. **Remove Element**: Given a set and an element, remove the element if it exists.
# 9. **Clear Set**: Create a new empty set from an existing set.
# 10. **Check if Set is Empty**: Determine if a set has any elements.
# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
# 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
# 14. **Find Maximum**: From a given set of numbers, find the maximum element.
# 15. **Find Minimum**: From a given set of numbers, find the minimum element.
# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
# 23. **Generate Random Set**: Create a set with a specified number of random integers within a certain range.

#Q1
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
print(union_set)   # {1, 2, 3, 4, 5}

#Q2
set_a = {1, 2, 3}
set_b = {2, 3, 4}
intersection_set = set_a & set_b
print(intersection_set)

#Q3
set_a = {1, 2, 3}
set_b = {2, 3, 4}
difference_set = set_a - set_b
print(difference_set)

#Q4
set_a = {1, 2}
set_b = {1, 2, 3, 4}
is_subset = set_a.issubset(set_b)
print(is_subset)

#Q5
my_set = {1, 2, 3}
element = 2
exists = element in my_set
print(exists)

#Q6
my_set = {1, 2, 3, 4}
length = len(my_set)
print(length)

#Q7
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)  

#Q8
my_set = {1, 2, 3}
element = 2
my_set.discard(element)
print(my_set)

#Q9
my_set = {1, 2, 3}
new_empty_set = set()
print(new_empty_set)

#Q10
my_set = set()
is_empty = len(my_set) == 0
print(is_empty)

#Q11
set_a = {1, 2, 3}
set_b = {2, 3, 4}
sym_diff = set_a ^ set_b
print(sym_diff)

#Q12
my_set = {1, 2, 3}
element = 4
my_set.add(element)
print(my_set)

#Q13
my_set = {1, 2, 3}
popped = my_set.pop()
print(popped)
print(my_set)

#Q14
my_set = {5, 1, 9, 3}
maximum = max(my_set)
print(maximum)

#Q15
my_set = {5, 1, 9, 3}
minimum = min(my_set)
print(minimum)

#Q16
my_set = {1, 2, 3, 4, 5, 6}
even_set = set()
for num in my_set:
    if num % 2 == 0:
        even_set.add(num)
print(even_set)

#Q17
my_set = {1, 2, 3, 4, 5, 6}
odd_set = set()
for num in my_set:
    if num % 2 != 0:
        odd_set.add(num)
print(odd_set) 

#Q18
range_set = set(range(1, 11))
print(range_set)

#Q19
list1 = [1, 2, 3]
list2 = [3, 4, 5]
merged_set = set(list1 + list2)
print(merged_set)

#Q20
set_a = {1, 2, 3}
set_b = {4, 5, 6}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)

#Q21
my_list = [1, 2, 2, 3, 3, 3, 4]
no_dupes_set = set(my_list)
no_dupes_list = list(no_dupes_set)
print(no_dupes_list)

#Q22
my_list = [1, 2, 2, 3, 3, 3, 4]
unique_count = len(set(my_list))
print(unique_count)


#Q23
import random
random_set = set(random.sample(range(1, 100), 5))
print(random_set)

# ### Dictionary Tasks
#
# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
# 3. **Count Keys**: Determine the number of keys in the dictionary.
# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary.
# 5. **Get All Values**: Create a list that contains all the values in the dictionary.
# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
# 8. **Clear Dictionary**: Create a new empty dictionary.
# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
# 11. **Update Value**: Given a dictionary, update the value for a specified key.
# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
# 21. **Sort Dictionary by Value**: Create a new dictionary sorted by values.
# 22. **Filter by Value**: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.
# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.

#Q1
my_dict = {"a": 1, "b": 2}
key = "c"
value = my_dict.get(key)
print(value)

#Q2
my_dict = {"a": 1, "b": 2}
key = "a"
exists = key in my_dict
print(exists)

#Q3
my_dict = {"a": 1, "b": 2, "c": 3}
count = len(my_dict)
print(count)

#Q4
my_dict = {"a": 1, "b": 2}
keys_list = list(my_dict.keys())
print(keys_list)

#Q5
my_dict = {"a": 1, "b": 2}
values_list = list(my_dict.values())
print(values_list)

#Q6
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2
print(merged)

#Q7
my_dict = {"a": 1, "b": 2}
key = "a"
if key in my_dict:
    del my_dict[key]
print(my_dict)


#Q8
new_empty_dict = {}
print(new_empty_dict)

#Q9
my_dict = {}
is_empty = len(my_dict) == 0
print(is_empty)

#Q10
my_dict = {"a": 1, "b": 2}
key = "a"
if key in my_dict:
    pair = (key, my_dict[key])
else:
    pair = None
print(pair)

#Q11
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 99
print(my_dict)

#Q12
my_dict = {"a": 1, "b": 2, "c": 1, "d": 1}
target_value = 1
count = 0
for v in my_dict.values():
    if v == target_value:
        count = count + 1
print(count)

#Q13
my_dict = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in my_dict.items():
    inverted[value] = key
print(inverted)


#Q14
my_dict = {"a": 1, "b": 2, "c": 1}
target_value = 1
matching_keys = []
for key, value in my_dict.items():
    if value == target_value:
        matching_keys.append(key)
print(matching_keys)

#Q15
keys_list = ["a", "b", "c"]
values_list = [1, 2, 3]
new_dict = dict(zip(keys_list, values_list))
print(new_dict)

#Q16
my_dict = {"a": 1, "b": {"x": 10}}
has_nested = False
for value in my_dict.values():
    if isinstance(value, dict):
        has_nested = True
print(has_nested)

#Q17
nested_dict = {"a": {"x": 10, "y": 20}, "b": 5}
outer_key = "a"
inner_key = "x"
value = nested_dict[outer_key][inner_key]
print(value)

#Q18
from collections import defaultdict
default_dict = defaultdict(lambda: "N/A")
default_dict["a"] = 1
print(default_dict["a"])
print(default_dict["z"])

#Q19
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
unique_count = len(set(my_dict.values()))
print(unique_count)

#Q20
my_dict = {"c": 3, "a": 1, "b": 2}
sorted_by_key = dict(sorted(my_dict.items()))
print(sorted_by_key)

#Q21
my_dict = {"a": 3, "b": 1, "c": 2}
sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_by_value)

#Q22
my_dict = {"a": 1, "b": 5, "c": 10, "d": 3}
filtered = {}
for key, value in my_dict.items():
    if value > 3:
        filtered[key] = value
print(filtered)

#Q23
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
common_keys = dict1.keys() & dict2.keys()
has_common = len(common_keys) > 0
print(has_common)


#Q24
pairs = (("a", 1), ("b", 2), ("c", 3))
new_dict = dict(pairs)
print(new_dict)

#Q25
my_dict = {"a": 1, "b": 2, "c": 3}
first_key = list(my_dict.keys())[0]
first_pair = (first_key, my_dict[first_key])
print(first_pair)
