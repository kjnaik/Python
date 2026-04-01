# Python
My python practice codes

**************************
Python in Kannada - Operators

None : is one datataype
not operater, which is opposite of that

in and not in operater
['c' in 'chandan']

*********************************
Python in Kannada - Lists Operations, Methods and Functions

.pop() = removes the last item
.pop(index)= removes the index item
.append(values)= added in the end of list
.insert(index, value)
.remove(value)= removes wherever it is
.clear= removes all values from list

insert is always = position -1

funation and methods

methods output are stored in the same variable
.sort()
.count() and .count(value)
.reverse()
.index(value)

funstions cahnges as to be stored into diff variable/list
len(list)
sorted(list)
sum(list)

*********************************
Python in Kannada - Tuples and Sets Operations & Difference

tubles can be modified

add(): Adds an element to the set.
remove(): Removes a specified element from the set. Raises an error if the element does not exist.
discard(): Removes a specified element without raising an error if it does not exist.
pop(): Removes a random element from the set.

Union:
The union of two sets combines all elements from both sets, removing duplicates.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
Intersection:
The intersection of two sets returns elements that are common to both sets.

intersection_set = set1 & set2  # Output: {3}
Difference:
The difference between two sets returns elements that are in the first set but not in the second.

difference_set = set1 - set2  # Output: {1, 2}
Symmetric Difference:
The symmetric difference returns elements that are in either of the sets but not in both.

sym_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}

*********************************
Python in Kannada - Dictionaries Operations, Methods and Functions

You can also use the get() method to access values, which is safer because it doesn’t throw an error if the key doesn’t exist.

print(karnataka_food.get("Mangaluru"))  # Output: Neer Dosa
print(karnataka_food.get("Shivamogga", "Not Found"))  # Output: Not Found