function binary_search(arr, x)
    low = 1
    high = length(arr)

    while low <= high
        mid = div(low + high, 2)  # integer division

        if arr[mid] == x
            return mid
        elseif arr[mid] < x
            low = mid + 1
        else
            high = mid - 1
        end
    end

    return -1   # not found
end

arr = [3, 8, 15, 20, 35, 50]

println("Results of binary_search: ", binary_search(arr, 20))  # Output: 4
println("Results of binary_search: ", binary_search(arr, 50))   # Output: -1
