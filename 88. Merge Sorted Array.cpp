#include <iostream>
using namespace std;
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int k = m+n-1;
        m--;
        n--;
        while(n>=0&&m>=0){
            nums1[k--] = nums1[m] > nums2[n] ? nums1[m--] : nums2[n--];
        }
        while(m>=0){
            nums1[k--] = nums2[m--];
        }
        return;
    }

};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}