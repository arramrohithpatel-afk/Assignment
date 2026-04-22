data = [10, 20, 30, 40, 50, 20, 30, 60, [70, 80], 90]
print("Original List:", data)

# 1. append()
data.append([100, 110])
print("After append [100,110]:", data)

# 2. extend()
data.extend([120, 130])
print("After extend 120,130:", data)

# 3. insert()
data.insert(2, 25)
print("After inserting 25 at index 2:", data)

# 4. remove()
data.remove(20)
print("After removing first 20:", data)

# 5. pop()
last_element = data.pop()
print("Popped last element:", last_element)
print("After pop:", data)

# 6. count()
count_30 = data.count(30)
print("Count of 30:", count_30)

# 7. index()
index_40 = data.index(40)
print("Index of 40:", index_40)

# 8. reverse()
data.reverse()
print("After reverse:", data)

# 9. sort issue
print("Trying to sort list with nested list...")
try:
    data.sort()
except Exception as e:
    print("Error while sorting:", e)

# Fix sorting (ignore nested list)
data_no_nested = [x for x in data if not isinstance(x, list)]
data_no_nested.sort()
print("Sorted list (without nested list):", data_no_nested)

# 10. flatten nested list
flattened = []
for item in data:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)

print("Flattened list:", flattened)