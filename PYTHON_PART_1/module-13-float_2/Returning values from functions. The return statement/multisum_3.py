def multisum(list1, list2):
    combined_list = list1 + list2
    total_length = 0
    for item in combined_list:
        total_length += len(item)
    return total_length


fruits = ["apple", "banana", "cherry", "date", "elderberry"]
vagtables = ["asparagus", "broccoli", "carrot", "daikon", "endive"]

result = multisum(fruits, vagtables)
print(result)