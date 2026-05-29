#include <stdio.h>
int main() {
    int n;
    printf("Enter the number of rows: ");
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) 
    {
        for (int j = 1; j <= n - i; j++) 
        {
            printf(" ");
        }
        
        int j;
        for ( j = 1; j <=i; j++)
        {
            printf("%d",j);
        }

        for (j=j-2 ; j>0 ; j--)
        {
            printf("%d",j);
        }
        
        printf("\n");

    }
    return 0;
}