N=int(input())
S=input()
arr=[]
v=0
for s in S:
	if s=="I":
		v+=1
		arr.append(v)
	else:
		v-=1
		arr.append(v)
print(max(0,max(arr)))