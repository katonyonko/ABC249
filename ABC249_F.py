import io
import sys

_INPUT = """\
6
5 1
2 4
2 -3
1 2
2 1
2 -3
1 0
2 -1000000000
10 3
2 3
2 -1
1 4
2 -1
2 5
2 -9
2 2
1 -6
2 5
2 -3
1 1
2 -10
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from heapq import heappop, heappush
  N,K=map(int,input().split())
  s=[list(map(int,input().split())) for _ in range(N)]
  s=s[::-1]
  ans=-10**20
  tmp=0
  k=0
  h=[]
  for i in range(N):
    t,y=s[i]
    if t==1:
      while k>K and len(h)>0:
        tmp-=heappop(h)
        k-=1
      if k<=K: ans=max(ans,y+tmp)
      k+=1
    else:
      if y>=0:
        tmp+=y
      else:
        heappush(h,-y)
        k+=1
  tmp=[s[i][1] for i in range(N) if s[i][0]==2]
  tmp.sort(reverse=True)
  tmp2=[tmp[i] for i in range(len(tmp)) if tmp[i]>=0]
  if len(tmp2)>=N-K: ans=max(ans,sum(tmp2))
  elif len(tmp)>=N-K: ans=max(ans,sum(tmp[:N-K]))
  print(ans)