#include <stdio.h>
#include <stdlib.h>
int main(void){
    FILE *file_out;
    file_out = fopen("ecs1_result.txt", "w");
    if(file_out = NULL){
        exit(1);
    }
    printf("Please input calculate times(n).\n");
    int n;
    scanf("%d",&n);
    printf("Please input late of change(r).\n");
    double r;
    scanf("%lf",&r);
    double x[n];
    printf("Please input initial number(x[0]).\n");
    scanf("%lf", &x[0]);
    printf("\n");
    for(int i=0; i < n+1; i++){
        x[i+1] = r * (1 - x[i]) * x[i];
        printf("%03d %lf\n", i, x[i]);
        fprintf(file_out, "%03d %lf\n", i, x[i]);
    }
    fclose(file_out);
    printf("Caluculate Complete.\n");
    return 0;
}