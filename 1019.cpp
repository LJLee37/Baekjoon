#include <iostream>
using namespace std;
int main()
{
    while (1){ //for debug
    int nums[10] = {0};
    int N = 0;
    cin >> N;
    /*
     * 1 < n < 10:
     *      i = 0 -> 0
     *      0 < i < n -> 1
     *      i = n -> 1
     *      i > n -> 0
     * 10 <= n <= 90, n % 10 = 0:
     *      i = 0 -> n
     *      0 < i < n -> 10 + n
     *      i = n -> n + 1
     *      i > n -> n
     *
     */
    for (int i = 1; i <= N; ++i)
    {
        int temp = i;
        while (temp > 0)
        {
            ++nums[temp % 10];
            temp /= 10;
        }
    }
    for (auto i : nums)
        cout << i << ' ';}
    return 0;
}
