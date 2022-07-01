import math
def getNextPalindrome(N):
    # Write your code here
    n = len(str(N))
    left = str(N)[:n//2]
    mid = str(N)[n//2]
    right = str(N)[n//2:]
    if N < 9:
        return N+1
    if N < 11:
        return 11
    if N == (10**n - 1):
        return N+2
    if left == right[::-1]:
        N = N+1
    if n % 2 == 0:
        if left[::-1] > right:
            return left + left[::-1]
        else:
            left = str(int(left) + 1)
            return left + left[::-1]
    else:
        if left[::-1] > right:
            return left + mid + left[::-1]
        else:
            if mid < '9':
                mid = str(int(mid)+1)
                return left + mid + left[::-1]
            else:
                mid = '0'
                left = int(left)+1
                return left + mid + left[::-1]
             
                
   
        
        


def main():

    N = int(input())
    result = getNextPalindrome(N);
    print(result)
if __name__ == "__main__":
    main()