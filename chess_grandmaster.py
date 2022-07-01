def countPlacements(xl1,xr1,yl1,yr1,xl2,xr2,yl2,yr2):
    # Write your code here
    first_pc_cord = []
    second_pc_cord = []
    count = 0
    for i in range(xl1,xr1+1):
        for j in range(yl1,yr1+1):
            first_pc_cord.append([i,j,(i+j)%2])
    for m in range(xl2,xr2+1):
        for n in range(yl2,yr2+1):
            second_pc_cord.append([m,n,(m+n)%2])
    for s in first_pc_cord:
        for t in second_pc_cord:
            if s != t and s[2]==t[2]:
                count+=1
    return count
	
	
	
def getPossible(A):

dict={}

B=[]

for i in A:

 dict[i]=1

A.sort()

for i in range(len(A)):

 if dict.get(A[i])==None:  

  dict[A[i]]=1

for i in range(len(A)):

 for j in range(i+1,len(A)):

  if A[j]!=A[i]:

   rus=A[j]-A[i]

   if dict.get(rus)==None:

    dict[rus]=1

    B.append(rus)  

while(len(B)!=0):

 c=B.pop(0)

 for i in range(len(A)):

  rus=abs(c-A[i])

  if dict.get(rus)==None:

   dict[rus]=1

   B.append(rus)

   

 A.append(c)

return len(dict.keys())

     

def main():

   N = int(input())

   A=[None]*N

   for j in range(N):

       A[j] = int(input())

   

   result = getPossible(A);

   print(result)

if __name__ == "__main__":

   main()

Explanation:

Please check my all sample test cases and  3 hidden test cases were correct in infosys sample test. Its not totally correct but if you find any corrections and can also help me please tell me.


