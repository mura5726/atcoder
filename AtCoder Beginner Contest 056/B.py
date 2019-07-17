W,a,b=map(int,input().split())
if b>=a:
	print(0 if b-a-W<1 else b-a-W)
else:
	print(0 if a-b-W<1 else a-b-W)
