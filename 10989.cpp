#include <cstdio>
using namespace std;
int main()
{
    int N = 0;
    scanf("%d", &N);
    int li[10001] = {0,};
    for (int i = 0; i < N; ++i)
    {
        int input = 0;
        scanf("%d", &input);
        ++li[input];
    }
    for (int i = 0; i < 10001; ++i)
        for (int j = 0; j < li[i]; ++j)
            printf("%d\n", i);
    return 0;
}
