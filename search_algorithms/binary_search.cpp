#include <iostream>
#include <vector>
#include <cmath>

int BinarySearch(const std::vector<int>& arr, int x) {
    int i = 0;
    int j = arr.size() - 1;
    int location;
    while (i < j) {
        int m = floor((i + j) / 2);

        if (x > arr[m]){
            i = m + 1;
        
        } else {
            j = m;
        }

    }

    if (x == arr[i]){
        location = i;
    } else {
        location = 0;
    }
    return location;
}

int main(){
    // Create Array in C++
    std::vector<int> arr = {1, 2, 3, 4, 5};

    // find element x & y
    int x = 3;
    int y = 5;

    // Search for elements of x & y
    int result_one = BinarySearch(arr, x);
    int result_two = BinarySearch(arr, y);

    if (result_one != -1) {
        std::cout << "Element " << x << " found at index: " << result_one << std::endl;
    } else {
        std::cout << "Element " << x << " not found." << std::endl;
    }

    if (result_two != -1) {
        std::cout << "Element " << y << " found at index: " << result_two << std::endl;
    } else {
        std::cout << "Element " << y << " not found." << std::endl;
    }
    return 0;
}