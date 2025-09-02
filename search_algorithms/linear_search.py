def linear_search(x, arr) -> int:
    i = 0
    while i < len(arr) and x != arr[i]:
        i += 1
    if i < len(arr):
        location = i
    else:
        location = 0
    return location

if __name__ == "__main__":
    # Test the linear_search function
    test_array = [1, 2, 3, 4, 5]
    print("Linear Search Result: ", linear_search(3, test_array))  # Output: 2
    print("Linear Search Result: ", linear_search(6, test_array))  # Output: 0