def binary_search(x, arr) -> int:
    i = 0
    j = len(arr) - 1
    while i < j:
        m = (i + j) // 2
        if x > arr[m]:
            i = m + 1
        else:
            j = m
    if x == arr[i]:
        location = i
    else:
        location = 0
    return location

if __name__ == "__main__":
    # Test the binary_search function
    test_array = [1, 2, 3, 4, 5]
    print("Binary Search Result: ", binary_search(3, test_array))  # Output: 2
    print("Binary Search Result: ", binary_search(6, test_array))  # Output: 0