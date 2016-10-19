#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
void quicksort (int a[], int lo, int hi)
{
//  lo is the lower index, hi is the upper index
//  of the region of array a that is to be sorted
    int i=lo, j=hi, h;

    // comparison element x
    int x=a[(lo+hi)/2];

    //  partition
    do
    {
        while (a[i]<x) i++;
        while (a[j]>x) j--;
        if (i<=j)
        {
            h=a[i]; a[i]=a[j]; a[j]=h;
            i++; j--;
        }
    } while (i<=j);

    //  recursion
    if (lo<j) quicksort(a, lo, j);
    if (i<hi) quicksort(a, i, hi);
}
int binary_search(std::vector<int> array,int l,int r,int value)
{
    int left=l;
    int right=r;

    while (left<=right)          //循环条件，适时而变
    {
        int middle=left + ((right-left)>>1);  //防止溢出，移位也更高效。同时，每次循环都需要更新。

        if (array[middle]>value)
        {
            right =middle-1;   //right赋值，适时而变
        }
        else if(array[middle]<value)
        {
            left=middle+1;
        }
        else
            return middle;
        //可能会有读者认为刚开始时就要判断相等，但毕竟数组中不相等的情况更多
        //如果每次循环都判断一下是否相等，将耗费时间
    }
    return -1;
}
class Solution {
public:
    vector<vector<int> > threeSum(vector<int>& nums) {

        vector<vector<int> > v;
        sort(nums.begin(),nums.end());
        if(nums.size() < 3) return v;
        if(nums[0]>0 || nums[nums.size()-1]<0) return v;
        int len = nums.size();
        int up1,up2;
        for (size_t i = 0; i < len;) {
          if (nums[i]>0) {
            break;
          }
          int indexlast = len;
          for (size_t j = i+1; j < len;) {

            int index = binary_search(nums,j+1, indexlast-1, -nums[i]-nums[j]);
            if (index != -1) {
              std::vector<int> tmp{nums[i],nums[j],nums[index]};
              v.push_back(tmp);
              indexlast = index;
            }
            do{
              ++j;
            }while(j < nums.size() && nums[j] == nums[j-1]);
          }
          do{
            ++i;
          }while(i < nums.size() && nums[i] == nums[i-1]);
        }
        return v;
    }
};
int main(int argc, char const *argv[]) {
  int v[] = {1,2,3,6,4};
  quicksort(v, 0, 4);
  for (size_t i = 0; i < 5; i++) {
    std::cout << v[i] << std::endl;
  }
  std::vector<int> nums{3,1,2,5,7,1};
  sort(nums.begin(),nums.end());
  for (size_t i = 0; i < nums.size(); i++) {
    std::cout << nums[i] << std::endl;
  }

  Solution hh;
  std::vector<int> num1{-1,0,1,2,-1,-4};

  hh.threeSum(num1);
  return 0;
}
