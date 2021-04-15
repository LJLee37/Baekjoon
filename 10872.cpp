#include <iostream>
using namespace std;
int main()
{
    int N;
    cin >> N;
    if (N == 0)
        N = 1;
    for (auto i = N - 1; i > 0; --i)
        N *= i;
    cout << N << endl;
    return 0;
}
