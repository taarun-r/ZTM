# CH-91 Function 


# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def hightest_even(li):
    even_num = []
    for item in li:
        if item % 2 == 0:
            even_num.append(item)
    return max(even_num)

print (hightest_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))






