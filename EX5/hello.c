#include<stdio.h>
#include<stdlib.h>
int main(){
    int n,k;
    scanf("%d",&n);
    int end = 1;
    int start = n;
    for(int i=0;i<n;i++){
        int lim = abs(start-end);
        if(start<end){
            k = start;
        }
        else{
            k = end;
        }
        for(int j=0;j<k-1;j++){
            printf(" ");
        }
        printf("%d",start);
        for(int j=0;j<lim-1;j++){
            printf(" ");
        }
        if(start!=end){
            printf("%d\n",end);
        }
        else{
            printf("\n");
        }

        start--;
        end++;
    }
}