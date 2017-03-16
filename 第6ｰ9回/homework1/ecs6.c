#include<stdio.h>
#define N 100
double next(double x, double r){
    double result = x;
    if(0<=x && x <1/2){
        result = 2*x;
    }else if(1/2<x && x<=1){
        result = 2*(1-x);
    }
    return result;
}

int main(void){
    int n;
    double r;
    double xn = 0.7;
    double xn1;
    scanf("%lf", &r);
    FILE *fp1;
    char filename
    if ((fp = fopen("smpl.txt", "r")) == NULL) {
        printf("file open error!!\n");
		exit(EXIT_FAILURE);	/* (3)エラーの場合は通常、異常終了する */
	}

    for(n=0; n<=N; n++){
        xn1 = next(xn, r);
        printf("%lf %lf\n", xn, xn1);
        printf("%lf %lf\n", xn1, xn1);
        xn = xn1;
        }
    return 0;
}