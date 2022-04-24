import io
import sys

_INPUT = """\
6
3 998244353
2 998244353
5 998244353
3000 924844033
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,P=map(int,input().split())
  dp=[[0]*N for _ in range(N+1)]
  dp[0][0]=1
  for i in range(N):
    for j in range(N):
      dp[i+1][j+1]=(dp[i+1][j+1]+)%P