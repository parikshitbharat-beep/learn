#include<stdio.h>
int main(){
    int r,j,num=0;
    printf("Enter the number of rows you want :");
    scanf("%d",&r);
    for (int i=1;i<=r;i++)
    {
        for (j=r+1-i;j>0;j--)
        {
            printf(" ");  
        }
        for (j=r;j>i-1;j--)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}