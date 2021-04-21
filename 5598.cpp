#include <iostream>
#include <string>
using namespace std;
int main()
{
    string input;
    cin >> input;
    for (auto& i : input)
        if (i != 0)
        {
            if (i < 'D')
                i += 23;
            else i -= 3;
        }
        else
            break;
    cout << input << endl;
}
