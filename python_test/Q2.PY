t = (10, 20, 30, 40, 50, 20, 60)
print("Original Tuple:", t)

# 1. count()
count_20 = t.count(20)
print("Count of 20:", count_20)

# 2. index()
index_40 = t.index(40)
print("Index of 40:", index_40)

# 3. convert → append → convert back
temp = list(t)
temp.append(70)
t = tuple(temp)
print("After adding 70:", t)

# 4. slicing (index 2 to 5)
slice_part = t[2:6]
print("Sliced tuple (index 2 to 5):", slice_part)

# 5. concatenate another tuple
t = t + (80, 90)
print("After concatenation (80,90):", t)

# 6. repeat tuple
repeated = t * 2
print("Repeated tuple:", repeated)

# 7. check if 50 exists
exists = 50 in t
print("Is 50 present?:", exists)

# 8. unpack tuple (first 7 elements)
a, b, c, d, e, f, g = t[:7]
print("Unpacked values:", a, b, c, d, e, f, g)

# 9. try modifying (will give error)
print("Trying to modify tuple...")
try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)

# 10. nested tuple
nested = (1, 2, (3, 4))
print("Nested tuple:", nested)
print("Access inner value (nested[2][1]):", nested[2][1])
