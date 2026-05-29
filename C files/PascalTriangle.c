#include<stdio.h>
// defining factorial
int factori(int n)
{
    int fact=1;
    for (int i=1 ; i <= n; i++)
    {
        fact*=i;
    }
    return fact;
}
// defining the nCr formula
int combi(int n, int r)
{
    int cmb=factori(n)/(factori(r)*factori(n-r));
    return cmb;
}
// printing the pascal triangle
int main()
{
    int n;
    printf("Enter the number of lines to print of the pascal triangle starting from 0 :");
    scanf("%d",&n);
    for (int i=0 ; i <= n; i++)
    {
        for (int j=0 ; j<=i ; j++)
        {
            printf("%d ",combi(i,j));
        }
        printf("\n");
    }
    return 0;
}