import math
import random

def find_closest_pair(points):
    """
    Finds the closest pair of points in a set of 2D points using a brute-force approach.

    Args:
        points: A list of tuples, where each tuple represents a point (x, y).

    Returns:
        A tuple containing:
        - The minimum distance between any two points.
        - A list of tuples, where each inner tuple contains a pair of points with that minimum distance.
    """
    num_points = len(points)
    if num_points < 2:
        return float('inf'), []

    min_dist = float('inf')
    closest_pairs = []

    # Iterate through all unique pairs of points
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            p1 = points[i]
            p2 = points[j]
            
            # Calculate Euclidean distance
            dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

            # Check if this is the new minimum distance
            if dist < min_dist:
                min_dist = dist
                closest_pairs = [(p1, p2)]
            # Check if this distance is equal to the current minimum
            elif dist == min_dist:
                closest_pairs.append((p1, p2))

    return min_dist, closest_pairs

def main():
    """
    Main function to generate points and find the closest pair,
    outputting to the console or a file based on the number of points.
    """
    # --- Configuration ---
    # Change this value to see different output behaviors
    # Try with values like 15, 25, 35, 50
    NUMBER_OF_POINTS = 25 
    
    # Generate a list of random 2D points
    # Using integers for cleaner output, but floats would also work
    points_A = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(NUMBER_OF_POINTS)]

    print(f"Generated {len(points_A)} points.")
    
    min_distance, pairs = find_closest_pair(points_A)

    # Prepare the results as a formatted string
    output_string = f"Closest distance found: {min_distance:.4f}\n"
    output_string += "Pairs with this distance:\n"
    for pair in pairs:
        output_string += f"  {pair[0]} and {pair[1]}\n"

    # Decide where to output the results
    if len(points_A) <= 30:
        print("\n--- Outputting to Command Window (A <= 30) ---")
        print(output_string)
    else:
        print("\n--- Outputting to File (A > 30) ---")
        file_path = 'closest_pair_results.txt'
        try:
            with open(file_path, 'w') as f:
                f.write(f"Analysis for a set of {len(points_A)} points.\n\n")
                f.write(output_string)
            print(f"Results successfully written to {file_path}")
        except IOError as e:
            print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
