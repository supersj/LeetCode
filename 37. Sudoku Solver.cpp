#include <iostream>
#include <vector>
#include <stack>
#include <deque>
#include <memory.h>
using namespace std;

typedef struct ele
{
    int x;
    int y;
    char value;
} ele;
ostream & operator<<(ostream & out, ele & A) {
    out << "x: " << A.x << " y: " << A.y << " value " << A.value;
    return out;
}
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int row[9] = {0};

        int cloum[9] = {0};
        int c[9] = {0};
        int idx = 0;
        for (int i = 0; i < 9; ++i)
        {
            for (int j = 0; j < 9; ++j)
            {
                if (board[i][j] != '.')
                {
                    idx = 1 << (board[i][j] - '0') ;
                    if ((row[i] & idx) > 0 ||
                            (cloum[j] & idx) > 0 ||
                            (c[(i / 3) * 3 + j / 3] & idx) > 0) return false;
                    row[i] |= idx;
                    cloum[j] |= idx;
                    c[(i / 3) * 3 + j / 3] |= idx;
                }
            }
        }
        return true;
    }
    void solveSudoku(vector<vector<char> >& board) {
        stack<ele> path;
        int curm = 1;
        int m = 0;
        int i = 0;
        int j = 0;
        while (1) {
            if (board[i][j] != '.') {
                if (i == 8 && j == 8)
                {
                    return;
                }
                if (j == 8)
                {
                    j = 0;
                    i++;
                } else {
                    j++;
                }
                continue;
            }
            char tmp;
            int m;
            for (m = curm; m <= 9; ++m)
            {

                board[i][j] = m + '0';
                if (isValidSudoku(board))
                {
                    path.push(ele{i, j, board[i][j]});
                    curm = 1;
                    break;
                } else {
                    board[i][j] = '.';
                }
            }
            if (m == 10) {
                if (path.size() >= 1)
                {
                    i = path.top().x;
                    j = path.top().y;
                    board[i][j] = '.';
                    curm = path.top().value - '0';
                    path.pop();
                    while (curm == 9 && path.size() >= 1) {
                        i = path.top().x;
                        j = path.top().y;
                        board[i][j] = '.';
                        curm = path.top().value - '0';
                        path.pop();
                    }
                    curm++;
                }
                continue;
            }
            if (i == 8 && j == 8)
            {
                return;
            }
            if (j == 8)
            {
                j = 0;
                i++;
            } else {
                j++;
            }
        }
    }
};

class SolutionFinal {
public:
    void solveSudoku(vector<vector<char>>& board) {
        int i, j;
        blank = 0;
        for (i = 0; i < 9; i++) {
            for (j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    dboard[i][j] = 0;
                    blank++;
                }
                else
                    dboard[i][j] = board[i][j] - '0';
            }
        }
        setCandidate();
        dfs();
        for (i = 0; i < 9; i++) {
            for (j = 0; j < 9; j++) {
                if (board[i][j] == '.')
                    board[i][j] = '0' + dboard[i][j];
            }
        }
    }

    bool dfs() {
        if (blank == 0) return true;
        int x, y, i, j, k;
        getCandidate(x, y);
        for (k = 1; k < 10; k++) {
            if (candidate[x][y][k] == 0) continue;
            dboard[x][y] = k;
            --blank;
            int candidate_copy[9][9][10];
            copyArr(candidate_copy, candidate);
            updateCandidate(x, y, k);
            if (dfs()) return true;
            copyArr(candidate, candidate_copy);
            ++blank;
            dboard[x][y] = 0;
        }
        return false;
    }

    void setCandidate() {
        int i, j, k, r, c;
        for (i = 0; i < 9; i++) {
            for (j = 0; j < 9; j++) {
                for (k = 1; k < 10; k++) {
                    candidate[i][j][k] = 1;
                }
            }
        }
        for (i = 0; i < 9; i++) {
            for (j = 0; j < 9; j++) {
                int digit = dboard[i][j];
                if (digit != 0) {
                    updateCandidate(i, j, digit);
                }
            }
        }
        for (i = 0; i < 9; i++) {
            for (j = 0; j < 9; j++) {
                int cnt = 0;
                for (k = 1; k < 10; k++) {
                    if (candidate[i][j][k] != 0)
                        ++cnt;
                }
                candidate[i][j][0] = cnt;
            }
        }
    }

    void getCandidate(int &x, int &y) {
        int i, j, min = 10;
        for (i = 0; i < 9; i++) {
            for (j = 0; j < 9; j++) {
                if (dboard[i][j] == 0 && candidate[i][j][0] < min) {
                    min = candidate[i][j][0];
                    x = i;
                    y = j;
                }
            }
        }
    }

    void updateCandidate(int x, int y, int d) {
        int i, j;
        for (i = 0; i < 9; i++) {
            if (dboard[i][y] == 0 && candidate[i][y][d] == 1) {
                candidate[i][y][d] = 0;
                candidate[i][y][0]--;
            }
        }
        for (j = 0; j < 9; j++) {
            if (dboard[x][j] == 0 && candidate[x][j][d] == 1) {
                candidate[x][j][d] = 0;
                candidate[x][j][0]--;
            }
        }
        int a = 3 * (x / 3), b = 3 * (y / 3);
        for (i = a; i < a + 3; i++) {
            for (j = b; j < b + 3; j++) {
                if (dboard[i][j] == 0 && candidate[i][j][d] == 1) {
                    candidate[i][j][d] = 0;
                    candidate[i][j][0]--;
                }
            }
        }
    }

    void copyArr(int dst[][9][10], int src[][9][10]) {
        memcpy(dst, src, sizeof(int) * 9 * 9 * 10);
    }

    int dboard[9][9];
    /* candidate[x][y][0] is the count of valid choices.
       candidate[x][y][digit] = 0 or 1, marks if a digit is valid at position (x,y) */
    int candidate[9][9][10];
    int blank; // the count of blank cell to be fill
};

int main(int argc, char const *argv[])
{
    Solution ll;
    std::vector<std::vector<char> > v;
    std::vector<string> vs{"..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6", "...2759.."};
    for (int i = 0; i < 9; ++i)
    {
        std::vector<char> tmp;
        // cout<< vs[i]<<endl;
        for (int j = 0; j < 9; ++j)
        {
            tmp.push_back(vs[i][j]);
        }
        v.push_back(tmp);
    }
    for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            cout << v[i][j];
        }
        cout << endl;
    }
    //
    ll.solveSudoku(v);
    for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            cout << v[i][j];
        }
        cout << endl;
    }
    return 0;
}