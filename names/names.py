import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
sorted_name = sorted(names_1)


def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return target
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
        return -1


for key in names_2:
    if binary_search_iterative(sorted_name, key) is not -1:
        duplicates.append(key)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
