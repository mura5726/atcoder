S=input()
T=int(input())
B=abs(S.count('L')-S.count('R'))+abs(S.count('U')-S.count('D'))
print(B+S.count('?') if T==1 else max(B-S.count('?'),(B-S.count('?'))%2))