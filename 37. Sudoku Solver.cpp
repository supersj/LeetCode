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
}ele;
ostream & operator<<(ostream & out, ele & A){
    out <<"x: "<< A.x <<" y: "<< A.y <<" value "<< A.value;
    return out;
}
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
     void solveSudoku(vector<vector<char> >& board) {
        stack<ele> path;
        int curm = 1;
        int m = 0;
        int i = 0;
        int j = 0;
        while(1){
            if (board[i][j] != '.') {
                if (i == 8 && j == 8)
                {
                    return;
                }
                if (j == 8)
                {
                    j = 0;
                    i++;
                }else{
                    j++;
                }
                continue;
            }
            char tmp;
            int m;
            for (m = curm; m <= 9; ++m)
            {

                board[i][j] = m+'0';
                if (isValidSudoku(board))  
                {   
                    path.push(ele{i,j,board[i][j]});
                    curm = 1;
                    break;
                }else{
                    board[i][j] = '.';
                }
            }
            if (m == 10){
                if (path.size()>=1)
                {
                    i = path.top().x;
                    j = path.top().y;
                    board[i][j] = '.';
                    curm = path.top().value - '0';
                    path.pop();
                    while(curm == 9 && path.size()>=1){
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
            }else{
                j++;
            }
        }
    }
};

int main(int argc, char const *argv[])
{
    Solution ll;
    std::vector<std::vector<char> > v;
    std::vector<string> vs{"..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."};
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
            cout<<v[i][j];
        }
        cout<<endl;
    }
    // 
    ll.solveSudoku(v);
        for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            cout<<v[i][j];
        }
        cout<<endl;
    }
    return 0;
}