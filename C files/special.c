#include<stdio.h>
int main(){
    int n;
    printf("Enter the number of lines :");
    scanf("%d",&n);
    for (int i=1;i<=2*n-1;i++)
    {
        for (int j = 1; j <= 2*n-1; j++)
        {
            int dist_i,dist_j,val;
            dist_i = (i<=n) ? i : 2*n-i;
            dist_j = (j<=n) ? j : 2*n-j;
            val = (dist_i<=dist_j) ? dist_i : dist_j;
            printf("%d ",val);
        }
        printf("\n");
    }
    return 0;
}