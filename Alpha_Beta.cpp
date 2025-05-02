#include <iostream>
#include <climits>


using namespace std;


int Alpha_Beta(int depth , int index , int table[] , bool isMax , int Alpha , int Beta , int h , int n)
{

    if(index >= n)
        return isMax ? INT_MIN : INT_MAX;

    if(depth == h || 2 * index + 1 >= n)
        return table[index];

    if(isMax)
    {
        int smaller = INT_MIN;
        for(int i = 1;i <= 2;i++)
        {
            int evl = Alpha_Beta(depth + 1 , 2 * index + i , table , false , Alpha , Beta , h , n);
            smaller = max(smaller , evl);
            Alpha = max(smaller , Alpha);
            if(Beta <= Alpha) break;
        }
        return smaller;
    }
        
    else
    {
        int great = INT_MAX;
        for(int i = 1;i <= 2;i++)
        {
            int evl = Alpha_Beta(depth + 1 , 2 * index + i , table , true , Alpha , Beta , h , n);
            great = min(great , evl);
            Beta = min(great , Beta);
            if(Beta <= Alpha) break;
        }
        return great;
    }
    
}

int log2(int n)
{
  return (n==1)? 0 : 1 + log2(n/2);
}

int main()
{
    int table[] = {3, 5, 2, 9, 12, 5, 23, 23};
    int n = sizeof(table)/sizeof(table[0]);
    int h = log2(n);
    int res = Alpha_Beta(0, 0, table, true , INT_MIN , INT_MAX , h , n);
    cout << "The optimal value is : " << res << endl; // The optimal value is : 12
    return 0;
}