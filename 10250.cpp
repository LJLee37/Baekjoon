#include <iostream>
using namespace std;
int main()
{
    int T = 0;
    int H, W, N;
    cin >> T;
    for (auto i = 0; i < T; ++i)
    {
        cin >> H >> W >> N;
        cout << (N - 1) % H + 1;
        int n = N % H;
        int h = N / H + 1 - (n == 0);
        if (h < 10)
            cout << '0';
        cout << h << endl;
    }
}

