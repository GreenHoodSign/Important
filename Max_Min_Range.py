def findMinSum(arr, n):
    CL = [0] * n
    CR = [0] * n
    q = []
    for i in range(0, n):
        while (len(q) != 0 and
               arr[q[-1]] >= arr[i]):
            CL[i] += CL[q[-1]] + 1
            q.pop()

        q.append(i)

    while len(q) != 0:
        q.pop()

    for i in range(n - 1, -1, -1):
        while (len(q) != 0 and
               arr[q[-1]] > arr[i]):
            CR[i] += CR[q[-1]] + 1
            q.pop()

        q.append(i)

    while len(q) != 0:
        q.pop()

    ans = 0


    for i in range(0, n):
        ans += (CL[i] + 1) * (CR[i] + 1) * arr[i]

    return ans



def findMaxSum(arr, n):
    CL = [0] * n
    CR = [0] * n
    q = []
    for i in range(0, n):
        while (len(q) != 0 and
               arr[q[-1]] <= arr[i]):
            CL[i] += CL[q[-1]] + 1
            q.pop()

        q.append(i)

    while len(q) != 0:
        q.pop()
    for i in range(n - 1, -1, -1):
        while (len(q) != 0 and
               arr[q[-1]] < arr[i]):
            CR[i] += CR[q[-1]] + 1
            q.pop()

        q.append(i)
    while len(q) != 0:
        q.pop()

    ans = 0
    for i in range(0, n):
        ans += (CL[i] + 1) * (CR[i] + 1) * arr[i]

    return ans


# Driver code
if __name__ == "__main__":
    arr = [1,1,3,4]
    n = len(arr)
    print(findMaxSum(arr, n)-findMinSum(arr, n))


