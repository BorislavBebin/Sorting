def heapify(data, asc, len_idx, i):
    cur = i
    left = 2 * i + 1
    right = 2 * i + 2

    if asc == 'asc':
        if left < len_idx and data[i] < data[left]:
            cur = left

        if right < len_idx and data[cur] < data[right]:
            cur = right

        if cur != i:
            data[i], data[cur] = data[cur], data[i]
            heapify(data, asc, len_idx, cur)
    else:
        if left < len_idx and data[i] > data[left]:
            cur = left

        if right < len_idx and data[cur] > data[right]:
            cur = right

        if cur != i:
            data[i], data[cur] = data[cur], data[i]
            heapify(data, asc, len_idx, cur)


def sort(data, asc):
    len_idx = len(data)

    for i in range(len_idx//2, -1, -1):
        heapify(data, asc, len_idx, i)

    for i in range(len_idx-1, 0, -1):
        data[i], data[0] = data[0], data[i]

        heapify(data, asc, i, 0)
    return data


data = [3, 5, 10, 8, 7]
ascending = input()
print(sort(data, ascending))