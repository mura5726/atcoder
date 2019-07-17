import sys
sys.setrecursionlimit(10**6)
N=int(input())
MOD=10**9+7
def seki(x):
	if x<2:
		return 1
	else:
		return x*seki(x-1)%MOD
print(seki(N)%MOD)