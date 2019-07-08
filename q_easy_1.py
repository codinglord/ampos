def solve_easy_1(arr_data):

    lstOfUniq = []
    for ival in arr_data:

        if arr_data.count(ival) == 1 : #only count 1 is allowed to to list
            lstOfUniq.append(ival)

    return [str(i) for i in lstOfUniq]


rs_1 = solve_easy_1([1, 1, 2, 2, 3])
print(', '.join(rs_1))


rs_2 = solve_easy_1([-1, 2, 4, 2, -1])
print(', '.join(rs_2))