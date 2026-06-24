# LISTS — ordered, mutable, allow duplicates
# ------------------------------------------
# The most common Python collection. Written with square brackets.

fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # apple — zero-indexed
print(fruits[-1])       # cherry — negative indexes count from the end
print(len(fruits))      # 3

# Lists are MUTABLE — you can change them in place
fruits[1] = "blueberry"
print(fruits)           # ['apple', 'blueberry', 'cherry']

# Lists can hold mixed types (though uniform types are more common)
mixed = [1, "two", 3.0, True, [5, 6]]

# ADDING items
fruits.append("date")          # add one item to the end
fruits.insert(0, "avocado")    # insert at a specific index
fruits.extend(["fig", "grape"]) # add multiple items
print(fruits)

# REMOVING items
fruits.remove("apple")   # remove by VALUE (first match)
popped = fruits.pop()    # remove & return the LAST item
first = fruits.pop(0)    # remove & return item at an index
del fruits[0]            # delete by index, no return
print(fruits, "| popped:", popped, "| first:", first)

# SLICING — [start:stop:step], stop is exclusive
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3]
print(nums[:3])     # [0, 1, 2]
print(nums[3:])     # [3, 4, 5]
print(nums[::2])    # [0, 2, 4] — every other
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] — reversed

# USEFUL methods
nums = [3, 1, 4, 1, 5, 9, 2]
print(sorted(nums))     # [1, 1, 2, 3, 4, 5, 9] — returns a NEW sorted list
print(nums)
nums.sort()             # sorts IN PLACE, returns None
print(nums)
print(nums.count(1))    # 2 — how many times 1 appears
print(nums.index(4))    # index of first 4
nums.reverse()          # reverse in place
print(nums)
print(sum([1, 2, 3]))   # 6
print(min([3, 1, 2]), max([3, 1, 2]))   # 1 3


# THE ALIASING / REFERENCE TRAP (heavily tested)
# A list variable holds a REFERENCE, not the data itself.
a = [1, 2, 3]
b = a              # b points to the SAME list, not a copy
b.append(4)
print(a)           # [1, 2, 3, 4] — changing b changed a!

# To get an independent copy:
c = a.copy()       # or a[:]  or  list(a)
c.append(5)
print(a)           # [1, 2, 3, 4] — unchanged
print(c)           # [1, 2, 3, 4, 5]
