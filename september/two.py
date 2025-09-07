def rotate_array(arr):
    if not arr:
        return
    result = []

    for i in arr:
        result.insert(0, i)

    return result




print(rotate_array([1,2,3,4,5]))


def rotate_using_slicing(arr):
    if not arr:
        return 
    
    return arr[::-1]


print(rotate_using_slicing([1,2,3,4,5]))




# Given a nested list like [1,[2,3],[4,[5]]], flatten it into [1,2,3,4,5].


def nested_list(arr):
    if not arr:
        return
    
    stack = arr[::-1]
    result = []

    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])
        else:
            result.append(item)

    return result


print(nested_list([1,[2,3],[4,[5]]]))








