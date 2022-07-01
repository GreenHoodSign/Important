n = int(input())
k = int(input())
left = []
right = []
for i in range(k):
left.append(int(input()))
for i in range(k):
right.append(int(input()))

a = []
b = []
#print(left, right)
for i in range(k):
a.append(int(input()))
for i in range(k):
b.append(int(input()))

list1 = [] # pickcost, opencost, left, right
for i in range(k):
list1.append([b[i], a[i], left[i], right[i]])
list1.sort()
cost = 0
i = 0
print(list1)
while n > 0 and i < k:
rng = (list1[i][3] - list1[i][2]) + 1
print(rng)
cost += (list1[i][1] + min(n, rng)*list1[i][0])
#print(cost)
i += 1
n -= rng
print(cost)