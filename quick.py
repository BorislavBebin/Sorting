def sort(data, asc):
    idx_len = len(data)
    if idx_len < 1:
        return data
    else:
        pivot = data.pop()
    greater = []
    lower = []

    for item in data:
        if asc == 'asc':
            if item > pivot:
                greater.append(item)
            else:
                lower.append(item)
        else:
            if item < pivot:
                greater.append(item)
            else:
                lower.append(item)
    return sort(lower, asc) + [pivot] + sort(greater, asc)


data = [3, 5, 10, 8, 7]
ascending = input()
print(sort(data, ascending))