# a = input()
# b = input()

# fa = [0] * 10
# fb = [0] * 10
# bulls = 0
# for i in range(len(a)):
#     if a[i] == b[i]:
#         bulls += 1
#     else:
#         fa[int(a[i])] += 1
#         fb[int(b[i])] += 1
# cows = 0
# for i in range(10):
#     cows += min(fa[i], fb[i])
    
# print(bulls)
# print(cows)










# hr_a, min_a = input().split(":")
# hr_b, min_b = input().split(":")
# c = input()

# dm = int(hr_a) * 60 + int(min_a)
# alm = int(hr_b) * 60 + int(min_b)
# tzdiff = int(c)
# arrival = alm - tzdiff * 60
# while arrival < dm:
#     arrival += 24*60

# dur = arrival - dm
# h = dur//60
# m = dur%60
# print(f"{h}:{m:02d}")


from collections import defaultdict, deque
def solve(n):
    ins = {}
    outs = {}
    conns = set()
    adj = defaultdict(list)
    for _ in range(n):
        s1, h1, s2, h2 = input().split()
        a = s1 + " " + h1
        b = s2 + " " + h2
        conns.add(a)
        conns.add(b)
        if a in outs:
            outs[a] += 1
        else:
            outs[a] = 1
        if b in ins:
            ins[b] += 1
        else:
            ins[b] = 1
        
        adj[a].append(b)
        adj[b].append(a)
        
        
    sc = []
    ec = []
    for v in conns:
        if v in outs:
            o = outs[v]
        else:
            o = 0
        if v in ins:
            i = ins[v]
        else:
            i = 0
        if o - i == 1:
            sc.append(v)
        elif i - o == 1:
            ec.append(v)
        elif i == o:
            continue
        else:
            print(-1)
            return

    if not sc and not ec:
        print(-1)
        return
    if len(sc) != 1 or len(ec) != 1:
        print(-1)
        return

    start = sc[0]
    end = ec[0]

    curr = start
    used = set()
    dq = deque([curr])
    used.add(curr)
    while dq:
        u = dq.popleft()
        for i in adj[u]:
            if i not in used:
                used.add(i)
                dq.append(i)
    
    for i in conns:
        if ((i in ins and ins[i] > 0) or (i in outs and outs[i] > 0)):
            if i not in used:
                print(-1)
                return
    
    print(f"{start} {end}")
    
n = int(input())
solve(n)



# n = int(input())
# freq = [0] * (201)
# bs = [0] * (219 // 20)
# ans = 0
# for _ in range(n):
#     v = int(input())
#     b = (v-1)//20
#     s = 0
#     for i in range(b):
#         s += bs[i]
    
#     start = b * 20 + 1
#     end = v
#     for i in range(start, end):
#         s += freq[i]
#     ans += s
#     freq[v] += 1
#     bs[b] += 1
# print(ans)


# def solve(k,n,m):
    
#     g = [[] for _ in range(k + 1)]
#     for _ in range(n):
#         u, v = map(int, input().split())
#         g[v].append(u)
    
#     prob = []
#     s = 0
#     for i in range(1, k + 1):
#         if not g[i]:
#             continue
#         s += 1
#         days = g[i]
#         for i in range(len(days) - 1):
#             prob.append(days[i+1] - days[i])

#     if m < s:
#         print(-1)
#         return

#     if m >= n:
#         print(0)
#         return
    
#     l = n - m
#     prob.sort()
#     res = 0
#     for i in range(l):
#         res += prob[i]
#     print(res)
# k,n,m = map(int, input().split())
# solve(k,n,m)



