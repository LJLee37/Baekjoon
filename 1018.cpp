// C++20 or later
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <bit>
using namespace std;
constexpr unsigned long long bw = 0b01010101;
constexpr unsigned long long wb = 0b10101010;
constexpr unsigned long long bwBOARD[8] = {bw, wb, bw, wb, bw, wb, bw, wb};
constexpr unsigned long long wbBOARD[8] = {wb, bw, wb, bw, wb, bw, wb, bw};
constexpr unsigned long long MASK = 0b11111111;
constexpr char BLACK = 'B';
constexpr char WHITE = 'W';
int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);
  int n, m;
  cin >> n >> m;
  vector<string> rawBoard(n);
  for (auto &i : rawBoard)
    cin >> i;
  vector<unsigned long long> board(n);
  for (int i = 0; i < n; i++)
    for (int j = 0; j < m; j++)
    {
      board[i] <<= 1;
      board[i] |= (rawBoard[i][j] == WHITE);
    }
  int answer = 64;
  for (int i = 0; i < n - 8 + 1; ++i)
  {
    for (int j = 0; j < m - 8 + 1; ++j)
    {
      int cntA = 0;
      int cntB = 0;
      for (int k = 0; k < 8; ++k)
      {
        cntA += popcount(((board[i + k] >> j) & MASK) ^ bwBOARD[k]);
        cntB += popcount(((board[i + k] >> j) & MASK) ^ wbBOARD[k]);
      }
      answer = min({answer, cntA, cntB});
    }
  }
  cout << answer;
  return 0;
}