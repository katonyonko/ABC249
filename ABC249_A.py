import io
import sys

_INPUT = """\
6
4 3 3 6 2 5 10
3 1 4 1 5 9 2
1 1 1 1 1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C,D,E,F,X=map(int,input().split())
  t=X//(A+C)*B*A+min(X%(A+C),A)*B
  a=X//(D+F)*E*D+min(X%(D+F),D)*E
  if t>a: print('Takahashi')
  elif t<a: print('Aoki')
  else: print('Draw')