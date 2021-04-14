#include <iostream>
using namespace std;
int main()
{
    int nums[10][4] = {
        {10,10,10,10}, {1,1,1,1}, {2,4,8,6}, {3,9,7,1},
        {4,6,4,6}, {5,5,5,5}, {6,6,6,6}, {7,9,3,1},
        {8,4,2,6}, {9,1,9,1}};
    int T = 0;
    cin >> T;
    for (auto i = 0; i < T; i++)
    {
        int a, b;
        cin >> a >> b;
        cout << nums[a % 10][(b - 1)% 4] << endl;
    }
}
