#include<cstdio>
using namespace std;
int A, B, C;
int X;
int solve(){
int ans = 0;
for(int i = 0; i <= A; ++i){
for(int j = 0; j <= B; ++j){
for(int k = 0; k <= C; ++k){
int tmp = i * 500 + j * 100 + k * 50;
if(tmp == X) ans++;
}
}
}
return ans;
}
int main(){
scanf("%d%d%d%d", &A, &B, &C, &X);
int ans = solve();
printf("%d\n", ans);
return 0;
}

