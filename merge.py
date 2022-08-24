def sort(data, asc):
    if len(data) > 1:
        midpoint = len(data)//2
        left = data[:midpoint]
        right = data[midpoint:]

        #  recursion
        sort(left, asc)
        sort(right, asc)

        #  merge
        x = 0 # left idx
        y = 0 # right idx
        z = 0 # merged array idx
        while x < len(left) and y < len(right):
            if asc == 'asc':
                if left[x] < right[y]:
                    data[z] = left[x]
                    x += 1
                else:
                    data[z] = right[y]
                    y += 1
                z += 1
            else:
                if left[x] > right[y]:
                    data[z] = left[x]
                    x += 1
                else:
                    data[z] = right[y]
                    y += 1
                z += 1

        while x < len(left):
            data[z] = left[x]
            x += 1
            z += 1
        
        while y < len(right):
            data[z] = right[y]
            y += 1
            z += 1


data = [3, 5, 10, 8, 7]
ascending = input()
sort(data, ascending)
print(data)