from collections import Counter
def makeEqual(A):
    # Write your code here
    count = 0
    idx = []
    map = Counter(A)
    value = sorted(map.values(),reverse=True)[0]
    for k,v in map.items():
        if v == value:
            key = k 
    for i,val in enumerate(A):
        if val == key:
            idx.append(i)
    new_set = set(idx)
    while len(new_set) < len(A):
        for j in idx[:]:
            l = (j + 1) % len(A)
            m = (j-1)%len(A)
            idx.append(m)
            idx.append(j)
            idx.append(l)
        count +=1
        new_set = set(idx)
    return count


def main():

    N = int(input())
    A=[None]*N
    for j in range(N):
        A[j] = int(input())
    
    result = makeEqual(A);
    print(result)
if __name__ == "__main__":
    main()