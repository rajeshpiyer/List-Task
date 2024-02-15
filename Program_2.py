def remove_duplicates(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 3, 3, 4, 4, 5]
print("Original List:", input_list)
print("List with Duplicates Removed:", remove_duplicates(input_list))
