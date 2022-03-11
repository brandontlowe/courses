numbers = [5, 7, 8, 12, 20]
doubled = [num * 2 for num in numbers]

print(doubled)

names = ["Dave", "John", "James", "Jesus"]
begins_with_j = [name for name in names if name.startswith("J")]
print(begins_with_j)