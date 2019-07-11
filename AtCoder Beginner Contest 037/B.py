import numpy as np
N,Q=map(int,input().split())
arr=np.zeros(N+1)
for _ in range(Q):
	L,R,T=map(int,input().split())
	arr[L:R+1]=T
for i in range(1,N+1):
	print(int(arr[i]))