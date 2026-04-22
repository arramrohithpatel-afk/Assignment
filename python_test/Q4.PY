student = {
    "name": "John",
    "age": 21,
    "marks": {"math": 80, "science": 90}
}

print("Original Dictionary:", student)

# 1. get()
name = student.get("name")
print("Name using get():", name)

# 2. add new key
student["grade"] = "A"
print("After adding grade:", student)

# 3. update()
student.update({"age": 22})
print("After updating age:", student)

# 4. pop()
removed_age = student.pop("age")
print("Removed age:", removed_age)
print("After removing age:", student)

# 5. popitem()
last_item = student.popitem()
print("Removed last inserted item:", last_item)
print("After popitem():", student)

# 6. keys()
print("All keys:", list(student.keys()))

# 7. values()
print("All values:", list(student.values()))

# 8. items()
print("All items:", list(student.items()))

# 9. setdefault()
student.setdefault("city", "Mumbai")
print("After setdefault city:", student)

# 10. merge dictionary
student.update({"gender": "Male"})
print("After merging new dictionary:", student)