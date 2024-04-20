# reuirement : we have a sorteed data already
def Recur_binary_search(data, find_point, start_point, end_point):
    # if points are confused like start is after the end or end is before the start
    if start_point > end_point:
        return False
    # Base case: check if find_point is at start_point or end_point
    if data[start_point] == find_point or data[end_point] == find_point:
        return True

    # Base case: if the subrange has only one element left
    # if the end and start point are same , this means we are reffring to the same point
    if start_point == end_point:
        return data[start_point] == find_point


    # Find the middle point of the subrange
    middle_point = (start_point + end_point) // 2  # mid point of data

    # If find_point is at the middle point, return True
    if data[middle_point] == find_point:
        return True

    # If find_point is smaller than the middle point, search the left half
    elif data[middle_point] > find_point:
        return Recur_binary_search(data, find_point, start_point, middle_point - 1)
    # replaced here end position with middle_point

    # If find_point is larger than the middle point, search the right half
    else:
        return Recur_binary_search(data, find_point, middle_point + 1, end_point)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
find_point = 6
print(Recur_binary_search(data, find_point, 0, len(data) - 1))  # Output: True
