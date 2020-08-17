def reverse(y):
    # y, res = abs(x), 0
    # # 则其数值范围为 [−2^31,  2^31 − 1]
    # boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    res = 0
    while y != 0:
        res = res * 10 + y % 10
        if res > 1e7:
            return 0
        y //= 10
    return res

n = int(input())
l = []
for _ in range(n):
    l += input().split()




n, m = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(m)]

def helper(l1, l2):
    for x in l1:
        if x in l2:
            return True
    return False

def helper2(l1, l2):
    return set(l1+list(l2))
def solution(data):
    cnt, res = 1, [data[0]]
    i = 1
    while i<m:
        for j in range(len(res)):
            if helper(data[i], res[j]):
                res[j] = helper2(data[i], res[j])
            else:
                res.append(data[i])
        i += 1
    return cnt, res

cnt, res = solution(data)
print(cnt)
for x in res:
    x = list(map(str, x))
    print(' '.join(x))


n, a, b = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]

res = 0
def recursion(cur_a,cur_b,i,r):
    global res

    if a == cur_a and b == cur_b:
        res = max(res, r)
        return
    if i==n:
        return
    # a
    recursion(cur_a+1, cur_b, i+1, r+data[i][0])
    # b
    recursion(cur_a, cur_b+1, i+1, r+data[i][1])
    # wu
    recursion(cur_a, cur_b, i+1, r)

recursion(0,0,0,0)
print(res)


