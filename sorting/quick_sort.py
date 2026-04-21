# Quick Sort
# Time complexity: O(n log n) average, O(n²) worst case
# Space complexity: O(log n)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Test
if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test)
    print("Sorted:  ", quick_sort(test))
