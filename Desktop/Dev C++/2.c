#include <stdio.h>

void calculate(int A,int B,int *S,int *P){
	*S=A+B;
	*P=A*B;
}



int main(){
	int aa,bb,ss,pp;
	scanf("%d",&aa);
	scanf("%d",&bb);
	calculate(aa,bb,&ss,&pp);
	printf("%d\n%d",ss,pp);
} //第23題  A、B傳值   S、P傳參考值 


