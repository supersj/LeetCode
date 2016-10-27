#include <iostream>
#include <vector>
#include <memory.h>
#include <bitset>
using namespace std;

class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {
        bool row[9];
        bool cloum[9];
        bool c[9];
        memset(row,false,sizeof(row));
        memset(cloum, false, sizeof(cloum));
        memset(c, false, sizeof(c));
        for (int i = 0; i < board.size(); ++i)
        {
            for (int j = 0; j < board[i].size(); ++j)
            {   
                char rtmp = board[i][j];
                char ctmp = board[j][i];
                if (rtmp != '.')
                {
                     if (row[rtmp - '1'])
                        return false;
                    row[rtmp- '1'] = true;
                }
                if (ctmp != '.')
                {
                     if (cloum[ctmp - '1'])
                        return false;
                    cloum[ctmp- '1'] = true;
                }
                int x = 3*(i/3%3)+(j/3%3);
                int y = 3*(i%3)+(j%3);
                char ttmp = board[x][y];
                if (ttmp != '.') {
                    if (c[ttmp-'1']) return false;
                    c[ttmp-'1'] = true;
                }
               
            }
            memset(row,false,sizeof(row));
            memset(cloum, false, sizeof(cloum));
            memset(c, false, sizeof(c));
        }
        return true;
    }
       bool isValidSudoku2(vector<vector<char>>& board) {
        int row[9] = {0};
        int cloum[9] = {0};
        int c[9] = {0};
        int idx = 0;
        for (int i = 0; i < 9; ++i)
        {
            for (int j = 0; j<9; ++j)
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
};

int main(int argc, char const *argv[])
{
    std::vector<string> v{".87654321","2........","3........","4........","5........","6........","7........","8........","9........"};
};
    std::vector<std::vector<char> > v = {};
    return 0;
}