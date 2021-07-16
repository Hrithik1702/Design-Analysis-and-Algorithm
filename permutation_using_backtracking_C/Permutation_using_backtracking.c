#include <stdio.h>
#include <stdlib.h>

int nc,c=0;
int main()
{
    printf("Enter the number of characters: ");
    scanf("%d",&nc);
    char str[nc];
    char ps[nc];
    printf("Enter the string: ");
    scanf("%s",&str);
    permute(str,0,nc,ps);
    printf("%d",c);
}
void permute(char s[],int pos,int n,char ps[])
{
    char temp[n] ;
    int k=0;
    int index=0;
    int omit[n];
    for(int i=0;i<n;i++)
    {
        int flag =1;
        for(int l=0;l<index;l++)
        {
            if(i==omit[l])
            {
                flag = 0;
            }
        }
        if(flag==1)
        {
            for(int k=i+1;k<n;k++)
            {
                if(s[k]==s[i])
                {
                    omit[index++] = k;
                }
            }
            int ind = 0;
            for(int j=0;j<n;j++)
            {
                if(i!=j)
                {
                    temp[ind]=s[j];
                    ind=ind+1;
                }
            }
            ps[pos] = s[i];
            if(pos<nc-1)
            {
                permute(temp,pos+1,n-1,ps);
            }
            else
            {
                printf("%s\n",ps);
                c++;
            }
        }

    }
}
