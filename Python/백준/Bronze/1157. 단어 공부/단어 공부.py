alp = list(input().upper())
alplist =list(set(alp))
cnt = []

for i in alplist:
    count = alp.count
    cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(alplist[(cnt.index(max(cnt)))])