# Pseudo Code for Closest Pairs

## a) Brute Force Euclidean Distance (Closest Pairs)

Brute-Force Closest-Pair Algorithm
Input: A list of n points P = {p1, p2, ..., pn} where each pi = (xi, yi).
Output: The smallest Euclidean distance min_dist between any pair of points, and a list of all pairs closest_pairs that are separated by this distance.

If n < 2, return infinity (or an error), as at least two points are needed.

Initialize min_dist to a very large number (infinity).

Initialize closest_pairs as an empty list.

For i from 0 to n-2:

 **For** j from i+1 to n-1:

     Let p_i = (x_i, y_i) and p_j = (x_j, y_j).

     Calculate `dist` = sqrt((x_i - x_j)^2 + (y_i - y_j)^2).

     **If** `dist` < `min_dist`:

         Set `min_dist` = `dist`.

        Clear the `closest_pairs` list.

        Add the pair (p_i, p_j) to `closest_pairs`.

    **Else if** `dist` == `min_dist`:

        Add the pair (p_i, p_j) to `closest_pairs`.

Return min_dist and closest_pairs.

Worst-Case Big-O Analysis
The primary operation in this algorithm is the distance calculation performed inside the nested loops. To determine the worst-case complexity, we count the number of times this operation is executed.

Outer Loop: The outer loop runs from i = 0 to n-2, which means it executes n-1 times.

Inner Loop: The inner loop runs from j = i+1 to n-1. The number of iterations depends on the value of i:

When i = 0, j runs from 1 to n-1 (n-1 times).

When i = 1, j runs from 2 to n-1 (n-2 times).

...

When i = n-2, j runs from n-1 to n-1 (1 time).

The total number of distance calculations is the sum of an arithmetic series:
(n-1) + (n-2) + ... + 1

This sum is equal to:
n * (n-1) / 2 = (n^2 - n) / 2

In Big-O notation, we focus on the dominant term and ignore constants and lower-order terms. The dominant term is n^2.

Therefore, the worst-case time complexity of the brute-force closest-pair algorithm is O(n^2).