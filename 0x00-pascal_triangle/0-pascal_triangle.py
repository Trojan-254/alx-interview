#!/usr/bin/python3
"""
Pascal’s triangle module
"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pascal_triangle = []
    for element in range(n):
        # Start each row with a 1
        new_list = [1]
        if element > 0:
            # Retrieve the previous row
            prev_row = pascal_triangle[element - 1]
            # Append the sum of pairs from the previous row
            for q in range(len(prev_row) - 1):
                next_value = prev_row[q] + prev_row[q + 1]
                new_list.append(next_value)
            # End each row with a 1
            new_list.append(1)
        
        # Add the new row to the triangle
        pascal_triangle.append(new_list)

    return pascal_triangle

