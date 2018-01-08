def my_min(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val


def read_file(file):
    lines = []
    with open(file) as file:
        for line in file:
            lines.append(line.strip())

        return lines


def my_3max(lines):
    max_lst = []
    for element in lines:
        max_lst.append(element)
        if len(max_lst) > 3:
            max_lst.remove(my_min(max_lst))
    return max_lst
