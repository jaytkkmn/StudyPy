import functools

test_arr = [
    [0, 8, 3, 2],
    [2, 1, 3, 0],
    [2, 6, 0, 6]
           ]

def findAllRange(arr, pool, length):
    if length >= 4:
        pool.append(arr[:])
        return

    for i in range(0, length + 1):
        arr[i], arr[length] = arr[length], arr[i]
        findAllRange(arr, pool, length + 1)
        arr[length], arr[i] = arr[i], arr[length]

def isTime(pool):
    res = []
    for i in pool:
        if not (((i[0] * 10 + i[1]) > 23) or ((i[2] * 10 + i[3]) > 59)):
            res.append(i)
    return res

def comp(a, b):
    for i in range(0, 4):
        if a[i] < b[i]:
            return 1
        elif a[i] == b[i]:
           continue
        else:
            return -1
    return 0

def solution(A, B, C, D):
    arr = [A, B, C, D]
    pool = []
    findAllRange(arr, pool, 0)
    pool = sorted(pool, key = functools.cmp_to_key(comp))
    pool = isTime(pool)
    if len(pool) <= 0:
        return 'NOT POSSIBLE'
    else:
        return '%d%d:%d%d' % (pool[0][0], pool[0][1], pool[0][2], pool[0][3])

if __name__ == '__main__':
    for i in test_arr:
        print(solution(i[0], i[1], i[2], i[3]))
