import io
import sys

_INPUT = """\
6
3
6 2 3
1
2
10
1 3 2 4 6 8 2 2 3 7
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  tmp=[0]*(2*10**5)
  ans=0
  for i in range(N):
    tmp[A[i]-1]+=1
  for i in range(2*10**5):
    for j in range(int((i+2)**.5)):
      if (i+1)%(j+1)==0:
        if j+1==(i+1)//(j+1): ans+=tmp[i]*tmp[j]*tmp[(i+1)//(j+1)-1]
        else: ans+=2*tmp[i]*tmp[j]*tmp[(i+1)//(j+1)-1]
  print(ans)