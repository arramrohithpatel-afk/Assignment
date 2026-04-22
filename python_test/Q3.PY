s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("Original s1:", s1)
print("Original s2:", s2)

# 1. add()
s1.add(60)
print("After adding 60 (duplicates not allowed):", s1)

# 2. update()
s1.update([70, 80, 90])
print("After update [70,80,90]:", s1)

# 3. remove()
s1.remove(20)
print("After removing 20:", s1)

# 4. discard()
print("Trying to discard 100 (not present)...")
s1.discard(100)
print("After discard 100 (no error):", s1)

# 5. pop()
popped_element = s1.pop()
print("Random element popped:", popped_element)
print("After pop:", s1)

# 6. copy()
copy_set = s1.copy()
copy_set.add(999)
print("Modified copy:", copy_set)
print("Original remains unchanged:", s1)

# 7. clear()
temp_set = s1.copy()
temp_set.clear()
print("After clear:", temp_set)
print("Length after clear:", len(temp_set))

# 8. remove duplicates using set
lst = [1, 2, 2, 3, 3, 4]
unique = set(lst)
print("List with duplicates:", lst)
print("After converting to set (duplicates removed):", unique)

# 9. convert set to list and sort
sorted_list = sorted(list(unique))
print("Sorted list from set:", sorted_list)