def sort(data, asc):
    idx_len = len(data)
    for i in range(1, idx_len):
        cur = data[i]
        while data[i - 1] > cur and i > 0 if asc == 'asc' else data[i - 1] < cur and i > 0:
            data[i - 1], data[i] = data[i], data[i - 1]
            i -= 1
    return data


data = [3, 5, 10, 8, 7]
ascending = input()
print(sort(data, ascending))