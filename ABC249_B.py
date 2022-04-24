import io
import sys

_INPUT = """\
6
AtCoder
Aa
atcoder
Perfect
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  c,s=0,0
  for i in range(len(S)):
    if S[i].upper()==S[i]:
      c=1
    if S[i].lower()==S[i]:
      s=1
  if c==1 and s==1 and len(set(S))==len(S):
    print('Yes')
  else: print('No')