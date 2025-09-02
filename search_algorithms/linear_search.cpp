#include <iostream>
#include <vector>

int LinearSearch(const std::vector<int>& arr, int x) {
    for (size_t i = 0; i < arr.size(); ++i) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main(){
    // Create Array in C++
    std::vector<int> arr = {1, 2, 3, 4, 5};

    // find element x & y
    int x = 3;
    int y = 5;

    // Search for elements of x & y
    int result_one = LinearSearch(arr, x);
    int result_two = LinearSearch(arr, y);

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