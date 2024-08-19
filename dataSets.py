# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

import random

small_data = [random.randint(0, 1000) for _ in range(10)]
medium_data = [random.randint(0, 10000) for _ in range(1000)]
large_data = [random.randint(0, 100000) for _ in range(10000)]

import time

# Function to measure execution time
def measure_time(data, sort_func):
    start_time = time.time()
    sort_func(data)
    end_time = time.time()
    return end_time - start_time

# Measure times for original Merge Sort
small_time = measure_time(small_data.copy(), merge_sort)
medium_time = measure_time(medium_data.copy(), merge_sort)
large_time = measure_time(large_data.copy(), merge_sort)

print(f"Small data set time: {small_time:.6f} seconds")
print(f"Medium data set time: {medium_time:.6f} seconds")
print(f"Large data set time: {large_time:.6f} seconds")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Hybrid Merge Sort: uses Insertion Sort for small subarrays
def hybrid_merge_sort(arr, threshold=10):
    if len(arr) > 1:
        if len(arr) <= threshold:
            insertion_sort(arr)
        else:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            hybrid_merge_sort(left_half, threshold)
            hybrid_merge_sort(right_half, threshold)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

# Measure times for Hybrid Merge Sort
small_hybrid_time = measure_time(small_data.copy(), hybrid_merge_sort)
medium_hybrid_time = measure_time(medium_data.copy(), hybrid_merge_sort)
large_hybrid_time = measure_time(large_data.copy(), hybrid_merge_sort)

print(f"Small data set hybrid time: {small_hybrid_time:.6f} seconds")
print(f"Medium data set hybrid time: {medium_hybrid_time:.6f} seconds")
print(f"Large data set hybrid time: {large_hybrid_time:.6f} seconds")

