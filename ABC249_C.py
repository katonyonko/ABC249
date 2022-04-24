import io
from re import I
import sys

_INPUT = """\
6
4 2
abi
aef
bc
acg
2 2
a
b
5 2
abpqxyz
az
pq
bc
cy
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  S=[input() for _ in range(N)]
  ans=0
  for i in range(1<<N):
    tmp=[0]*26
    for j in range(N):
      if (i>>j)&1==0: continue
      for k in range(len(S[j])):
        tmp[ord(S[j][k])-ord('a')]+=1
    ans=max(ans,sum([1 for i in range(26) if tmp[i]==K]))
  print(ans)