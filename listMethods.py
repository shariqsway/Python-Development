numbers = [5, 2, 1, 7, 4]

# Add new item to the list
numbers.append(20)
print(numbers)

# Add to certain index
numbers.insert(0, 10)
print(numbers)

# Remove an item
numbers.remove(5)
print(numbers)

# Remove last item
numbers.pop()
print(numbers)

# Index of first occurrence of value
print(numbers.index(7))

# Check existence of some value (Returns boolean)
print(7 in numbers)

# Count value occurrences
print(numbers.count(4))

# Sort the list - ascending
numbers.sort()
print(numbers)

# Sort the list - descending
numbers.sort()
numbers.reverse()
print(numbers)

# Copy the list
numbers2 = numbers.copy()
print(numbers2)

# Remove all items
numbers.clear()
print(numbers)
