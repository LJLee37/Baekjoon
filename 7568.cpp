#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n;
  cin >> n;
  vector<int[4]> people(n);
  for (int i = 0; i < n; i++)
  {
    cin >> people[i][1] >> people[i][2];
    people[i][0] = i;
    people[i][3] = 1;
  }
  for (int i = 0; i < n - 1; i++)
    for (int j = i + 1; j < n; j++)
      if (people[i][1] > people[j][1] && people[i][2] > people[j][2])
        people[j][3]++;
      else if (people[i][1] < people[j][1] && people[i][2] < people[j][2])
        people[i][3]++;
  for (const auto &person : people)
    cout << person[3] << " ";
  return 0;
}