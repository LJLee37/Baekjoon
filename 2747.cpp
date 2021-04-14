#include <iostream>
using namespace std;
int main()
{
    int fibo[3] = {0, 1, 1};
    int n;
    cin >> n;
    if (n < 3)
    {
        cout << fibo[n] << endl;
        return 0;
    }
    for (auto i = 3; i <= n; ++i)
        fibo[i % 3] = fibo[(i - 1) % 3] + fibo[(i - 2) % 3];
    cout << fibo[n % 3] << endl;
    return 0;
}
