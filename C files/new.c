#include <stdio.h>
void swap(int a, int b){
    int temp=a;
    a=b;
    b=temp;
    return ;
}
int main(){
    int a,b;
    printf("Enter 2 numbers to be swapped :");
    scanf("%d %d",&a,&b);
    printf("The swapped numbers are :%d, %d",a,b);
    swap(a,b);
}