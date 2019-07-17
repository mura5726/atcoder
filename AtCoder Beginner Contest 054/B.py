N,M=map(int,input().split())
A=[input() for _ in range(N)]
B=[input() for _ in range(M)]
arr=[]
for i in range(N-M+1):
	for j in range(N-M+1):
		l=list(map(lambda x:x[j:j+M],A[i:i+M]))
		arr.append(all([l[k]==B[k] for k in range(M)]))
print("Yes" if any(arr) else "No")