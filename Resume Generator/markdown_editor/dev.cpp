#include <iostream>
#include<vector>
#include<bits/stdc++.h>
#include<algorithm>
#include<map>
using namespace std;
int fu(){
    static int x = 90;
    x = 80;
    return --x;
}
int main()
{

    int x = 0;
    int y = x++;
    cout << y;

    return 0;
}