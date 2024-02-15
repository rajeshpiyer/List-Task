tuple1 = (1, 2, 3, 4, 5, 2, 3, 6, 7, 2)
repeated_items = []
for item in tuple1:
    if tuple1.count(item) > 1 and item not in repeated_items:
        repeated_items.append(item)
print("Original Tuple : ",tuple1)
print("Repeated Items : ",repeated_items)
