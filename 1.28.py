def is_sublist(list1, list2):
    if len(list2) == 0:
        return True
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i + len(list2)] == list2:
            return True
    return False



list1 = [1, 2, 3, 4]
list2 = [2, 3]
print(is_sublist(list1, list2))
