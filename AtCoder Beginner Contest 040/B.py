n=int(input())
ans=10**6
for i in range(1,n+1):
	t=abs(n-i*2)+n-(n-i)*(i)
	ans = min(ans, t if t>0 else ans)
print(ans)