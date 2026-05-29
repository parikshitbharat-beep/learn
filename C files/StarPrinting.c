#include<stdio.h>
int main(){
    int r,c;
    printf("Enter the number of rows you want :");
    scanf("%d",&r);
    printf("Enter the Number of columns you want :");
    scanf("%d",&c);
    for (int i=1;i<=r;i++)
    {
        if (i==(r+1)/2){
            for (int k =1;k<=r;k++) printf("*");
            printf("\n");
            continue;
        }
        for (int j=0;j<r;j++)
        {
            if (j==(r+1)/2-1){
                printf("*");
                continue;
            }
            printf(" ");
        }
        printf("\n");
    }
    return 0;
}