def rec_max(lst):
    if len(lst) == 1:
        print(f'max in {lst}: {lst[0]}')
        return lst[0]
    max_in_sublist = rec_max(lst[1:])
    if lst[0] > max_in_sublist:
        print(f'max in {lst}: {lst[0]}')
        return lst[0]
    print(f'max in {lst}: {max_in_sublist}')
    return max_in_sublist

res = rec_max([3, 7, 1, 8, 2, 10, 5])
