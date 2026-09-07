import random
import time


def selection_sort(arr):
    numsofelement = len(arr)

    for i in range(numsofelement):
        min_index = i

        for j in range(i + 1, numsofelement):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]

    smaller_number = []
    greater_number = []

    for number in arr[:-1]:
        if number <= pivot:
            smaller_number.append(number)
        else:
            greater_number.append(number)

    return quick_sort(smaller_number) + [pivot] + quick_sort(greater_number)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    return merge(left, right)


def main():
    numbers = [random.randint(1, 100) for _ in range(20)]

    print("Random list:", numbers)

    total_start = time.perf_counter()

    start = time.perf_counter()
    selection_result = selection_sort(numbers.copy())
    end = time.perf_counter()
    print("\nSelection Sort:", selection_result)
    print("Execution time:", end - start, "seconds")

    start = time.perf_counter()
    insertion_result = insertion_sort(numbers.copy())
    end = time.perf_counter()
    print("\nInsertion Sort:", insertion_result)
    print("Execution time:", end - start, "seconds")

    start = time.perf_counter()
    quick_result = quick_sort(numbers.copy())
    end = time.perf_counter()
    print("\nQuick Sort:", quick_result)
    print("Execution time:", end - start, "seconds")

    start = time.perf_counter()
    merge_result = merge_sort(numbers.copy())
    end = time.perf_counter()
    print("\nMerge Sort:", merge_result)
    print("Execution time:", end - start, "seconds")

    total_end = time.perf_counter()

    print("\nTotal execution time:", total_end - total_start, "seconds")

if __name__ == "__main__":
    main()