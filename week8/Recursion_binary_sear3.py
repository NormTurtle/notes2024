def Recur_binary_search(data, find_point, start_point, end_point):
    # Check if start_point and end_point are valid indices
    if start_point > end_point:
        return False

        # Base case: check if find_point is at start_point or end_point
    if data[start_point] == find_point or data[end_point] == find_point:
        return True
    # Base case: if the subrange has only one element left
    if start_point == end_point:
        return data[start_point] == find_point

    # Find the middle point of the subrange
    middle_point = (start_point + end_point) // 2

    # If find_point is at the middle point, return True
    if data[middle_point] == find_point:
        return True

    # If find_point is smaller than the middle point, search the left half
    elif data[middle_point] > find_point:
        return Recur_binary_search(data, find_point, start_point, middle_point - 1)

    # If find_point is larger than the middle point, search the right half
    else:
        return Recur_binary_search(data, find_point, middle_point + 1, end_point)


# Example usage:
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_point = 6
print(Recur_binary_search(data, find_point, 0, len(data) - 1))  # Output: True
