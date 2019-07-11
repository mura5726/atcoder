N=int(input())
S=[input() for _ in range(N)]
for i in range(N):
	for j in range(N):
		print(S[-j][-i], end="\n") if j == N-1 else print(S[-j][-i], end="") 