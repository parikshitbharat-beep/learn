#include<stdio.h>
int main(){
    int r,j,num=0;
    printf("Enter the number of rows you want :");
    scanf("%d",&r);
    for (int i=r;i>0;i--)
    {
        for (j=1;j<=i-1;j++)
        {
            printf(" ");  
        }
        for (j=1;j<=r;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}