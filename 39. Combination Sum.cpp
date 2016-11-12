#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<int> path;
        combine(candidates, 0, target, path);
        return result;
    }

private:
    vector<vector<int> > result;

    void combine(vector<int>& candidates, int ix, int remain, vector<int>& path) {
        if (remain == 0) {
            result.push_back(path);
            return;
        }

        for (int i = ix; i < candidates.size(); ++i) {
            if (remain < candidates[i])   // prunning
                return;

            path.push_back(candidates[i]);
            combine(candidates, i, remain - candidates[i], path);
            path.pop_back();
        }
    }
};

//函数功能 ： 从数列1,2...n中随意取几个数，使其和等于m  
//函数参数 ： n为当前最大值，m为剩余值，flag标记选中与否，len为flag的容量  
//返回值 ：   无  
void BagProblem_Solution1(int n, int m, int *flag, int len)  
{  
    if(n < 1 || m < 1)  
        return;  
  
    if(n < m)  
    {  
        flag[n-1] = 1;  
        BagProblem_Solution1(n-1, m-n, flag, len); //选了n  
        flag[n-1] = 0;  
        BagProblem_Solution1(n-1, m, flag, len);   //不选n  
    }  
    else  
    {  
        flag[m-1] = 1;  //n>=m，选中m即可  
        for(int i = 0; i < len; i++)  
        {  
            if(flag[i] == 1)  
                cout<<i+1<<' ';  
        }  
        cout<<endl;  
        flag[m-1] = 0; //不选m，继续递归。比如n = 10,m = 8，求出{1, 7}后，仍需继续，{1,3,4} {1,2,5}都是解  
        BagProblem_Solution1(m-1, m, flag, len);  
    }  
}  

int main(int argc, char const *argv[])
{
    /* code */
    int flag[10] = {0};
    BagProblem_Solution1(10,22,flag,10);
    return 0;
}