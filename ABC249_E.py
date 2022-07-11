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
  dp=[[0]*(N+2) for _ in range(N+1)]
  diff=[[0]*(N+2) for _ in range(N+2)]
  dp[0][0]=1
  for i in range(N+1):
    if i==0: a=26
    else: a=25
    for j in range(N+2):
      if i>0 and j>0: dp[i][j]=(dp[i-1][j]+diff[i][j])%P
      diff[min(i+1,N+1)][min(j+2,N+1)]=(diff[min(i+1,N+1)][min(j+2,N+1)]+a*dp[i][j])%P
      diff[min(i+10,N+1)][min(j+2,N+1)]=(diff[min(i+10,N+1)][min(j+2,N+1)]-a*dp[i][j])%P
      diff[min(i+10,N+1)][min(j+3,N+1)]=(diff[min(i+10,N+1)][min(j+3,N+1)]+a*dp[i][j])%P
      diff[min(i+100,N+1)][min(j+3,N+1)]=(diff[min(i+100,N+1)][min(j+3,N+1)]-a*dp[i][j])%P
      diff[min(i+100,N+1)][min(j+4,N+1)]=(diff[min(i+100,N+1)][min(j+4,N+1)]+a*dp[i][j])%P
      diff[min(i+1000,N+1)][min(j+4,N+1)]=(diff[min(i+1000,N+1)][min(j+4,N+1)]-a*dp[i][j])%P
      diff[min(i+1000,N+1)][min(j+5,N+1)]=(diff[min(i+1000,N+1)][min(j+5,N+1)]+a*dp[i][j])%P
      diff[min(i+3001,N+1)][min(j+5,N+1)]=(diff[min(i+3001,N+1)][min(j+5,N+1)]-a*dp[i][j])%P
  print(sum(dp[N][:N])%P)