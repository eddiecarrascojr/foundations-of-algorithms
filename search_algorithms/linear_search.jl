function LinearSearch(x, arr)
   for i in eachindex(arr)   # iterate through valid indices
        if arr[i] == x
            return i   # return index if found
        end
    end
    return -1   # return -1 if not found
end

arr = [10, 25, 30, 5, 8]

print("Results of LinearSearch: ", LinearSearch(25, arr), "\n")
print("Results of LinearSearch: ", LinearSearch(8, arr), "\n")