N=int(input())
T=list(map(int,(input().split())))
M=int(input())
for _ in range(M):
	t=T[:]
	p,x=map(int,input().split())
	t[p-1]=x
	print(sum(t))