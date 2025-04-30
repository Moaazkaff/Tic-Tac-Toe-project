#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int minmax(int depth , int index , int table[] , bool isMax , int h , int n)
{
    if(index >= n) 
        return isMax ? INT_MIN : INT_MAX; // If the index is out of bounds, return extreme values
    
    if(depth == h || (index * 2 + 1) >= n) return table[index];

    if(isMax) return max(minmax(depth + 1 , index * 2 + 1 , table , false , h , n) , minmax(depth + 1 , index * 2 + 2 , table , false , h , n));

    else return min(minmax(depth + 1 , index * 2 + 1 , table , true , h , n) , minmax(depth + 1 , index * 2 + 2 , table , true , h , n));
}

int log2(int n)
{
  return (n==1)? 0 : 1 + log2(n/2);
}

int main()
{
    // int scores[] = {7, 13, 5, 10, 8, 4, 6, 2};
    // int scores[] = {3, 5, 2, 9, 12, 5, 23, 23};
    int scores[] = {3, 5, 2, 9, 12};  
    int n = sizeof(scores)/sizeof(scores[0]);
    int h = log2(n);
    int res = minmax(0, 0, scores, true , h , n);
    cout << "The optimal value is : " << res << endl;
    return 0;
}