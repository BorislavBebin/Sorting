def sort(data, asc):
    idx_len = len(data) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(idx_len):
            if asc == 'asc':
                if data[i] > data[i+1]:
                    sorted=False
                    data[i],data[i+1] = data[i+1],data[i]
            else:
                if data[i] < data[i+1]:
                    sorted=False
                    data[i],data[i+1] = data[i+1],data[i]
    return data


data = [3, 5, 10, 8, 7]
ascending = input()
print(sort(data, ascending))