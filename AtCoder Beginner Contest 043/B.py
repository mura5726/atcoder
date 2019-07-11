s=input()
c=s.count('B')

print("".join(list(map(lambda x:x[0:len(x)-1],s[0:len(s)-1])))+s[-1])