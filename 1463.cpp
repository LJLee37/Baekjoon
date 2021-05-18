#include <iostream>
using namespace std;
constexpr int min(int lhs, int rhs){return lhs < rhs ? lhs : rhs;}
class ArrContainer
{
    public:
    constexpr ArrContainer() : arr()
    {
        for (auto i = 0; i < 1000001; ++i)
            arr[i] = i - 1;
        for (auto i = 0; i < 1000001; ++i)
        {
            if (i < 1000000)
                arr[i + 1] = min(arr[i] + 1, arr[i + 1]);
            if (i * 2 <= 1000000)
                arr[i * 2] = min(arr[i] + 1, arr[i * 2]);
            if (i * 3 <= 1000000)
                arr[i * 3] = min(arr[i] + 1, arr[i * 3]);
        }
    }
    int arr[1000001];
};
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int n = 0;
    cin >> n;
    ArrContainer a;
    cout << a.arr[n];
    return 0;
}
