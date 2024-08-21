#include <utility>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const auto compare = [](const pair<int, int> &a, const pair<int, int> &b)
{
  return a.second == b.second ? a.first < b.first : a.second < b.second;
};
int main()
{
  int n;
  cin >> n;
  vector<pair<int, int>> coordinates(n);
  for (int i = 0; i < n; i++)
    cin >> coordinates[i].first >> coordinates[i].second;
  sort(coordinates.begin(), coordinates.end(), compare);
  for (const auto &coordinate : coordinates)
    cout << coordinate.first << ' ' << coordinate.second << '\n';
  return 0;
}