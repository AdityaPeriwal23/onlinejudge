#include<bits/stdc++.h>
using namespace std;
#define endl "\n"
long long int solve(long long int n,vector<long long int>&t)
{
    if(n==0)
    return 1;
    if(t.at(n)!=-1)
    return t.at(n);
    long long int j=0;
    for(long long int i=1;i<=6;i++)
    {
        if(i>n)
        break;
        j+=(solve(n-i,t)%1000000007)%1000000007;
    }
    return t.at(n)=j%1000000007;
}
int main() 
{
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
freopen ("output.txt","w",stdout); freopen ("input.txt","r",stdin);
   long long int n;
   cin>>n;
   vector<long long int>t(n+1,-1);
   cout<<solve(n,t)%1000000007;
   return 0;
}