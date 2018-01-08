from operator import itemgetter

travel_dates = [1, 3, 5, 8, 9, 19]

def normalize(date):

    L = 30
    d1 = []
    for i in range(L):
        d1.append(1 if (i+1) in date else 0)
    return d1

def group_func(d):
    L=len(d)
    result = []
    for i in range(L):
        s = sum(d[i:i+7])
        result.append((i,s))
    return result

d1 = normalize(travel_dates)

mincost = 0

while True:
    a = group_func(d1)
    a.sort(key= itemgetter(1))
    m = a[-1][1]
    if m < 4:
        break
    for q in a:
        if q[1] == m:
            w = q
            break
    d1[w[0]:w[0]+7] = [0]*7
    mincost = mincost + 7

mincost = mincost + d1.count(1)*2
answer = min(25, mincost)
print("minimum cost:", answer)

