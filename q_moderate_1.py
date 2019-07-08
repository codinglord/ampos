from functools import reduce


def solve_moderate_1(arr_data):

    lstOfSum =[]

    for idx,ival in enumerate(arr_data):

        iarr = arr_data.copy() #clone array
        iarr.pop(idx) #exclude current item
        irs = reduce(lambda x, y: x * y, iarr) #multiply cross product
        lstOfSum.append(irs) #add item to array

    return [str(i) for i in lstOfSum]



rs_2 = solve_moderate_1([1, 2, 3, 4])
print(', '.join(rs_2))