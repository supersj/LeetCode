
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
#include <unordered_map>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ni() { int a; scanf( "%d", &a ); return a; }
double nf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; string ns() { scanf( "%s", sbuf ); return sbuf; }
long long nll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef stringstream ss;
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef unordered_map<string,int> umsi;
typedef unordered_map<int,int>  umii;

class Solution {
public:
        vi helper(vi nums,int k){
        int len1 = int(nums.size());
        if(len1 <= k){
            return nums;
        }
        vi result(k,0);
        int dindex = 0,i = 0,t = 0;
        for ( i = 0; i < len1; ++i) {
            if(i == len1 - k){
                for (int l = dindex + 1; l < k; ++l) {
                    result[l] = 0;
                }
                while (i < len1) {
                    for (int j = 0; j < k; ++j) {
                        if (nums[i] > result[j]) {
                            if (k - j > len1 - i) {
                                continue;
                            }
                            result[j] = nums[i];
                            for (int l = j+1; l < k; ++l) {
                                result[l] = 0;
                            }
                            break;
                        }
                    }
                    i++;
                }
                break;
            }
            for (int j = t; j < k; ++j) {
                if(nums[i] > result[j]){
                    result[j] = nums[i];
                    dindex = j;
                    for (int l = j+1; l <k ; ++l) {
                        result[l] = 0;
                    }
                    break;
                }
            }
        }
        return result;
    }
    bool compare(vi nums1, int start1, vi nums2, int start2) {
        for (; start1 < nums1.size() && start2 < nums2.size(); start1++, start2++) {
            if (nums1[start1] > nums2[start2]) return true;
            if (nums1[start1] < nums2[start2]) return false;
        }
        return start1 != nums1.size();
    }
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        int index_1 = 0,index_2 = 0;
        int len1 = int(nums1.size());
        int len2 = int(nums2.size());
        vi v1 = helper(nums1,k);
        vi v2 = helper(nums2,k);
        vi result;
        vi tmp(k,0);
        vi t1,t2;
        int t = int(v1.size());
        for (int i = 0; i <= min(t,k) ; ++i) {
            result.clear();
            if(k-i > int(v2.size())){
                continue;
            }
            int cnt = 0;
            t1 = helper(v1,i);
            t2 = helper(v2,k-i);
            int index1 = 0,index2 = 0;
            while((cnt < k) && (index1 < t1.size()) && (index2 < t2.size())) {
                cnt += 1;
                if(t1[index1] > t2[index2]){
                    result.pb(t1[index1]);
                    index1 ++;
                }else if(t1[index1] < t2[index2]){
                    result.pb(t2[index2]);
                    index2 ++;
                }else{
                    if(compare(t1,index1+1,t2,index2+1)){
                        result.pb(t1[index1]);
                        index1 ++;
                    }else{
                        result.pb(t2[index2]);
                        index2 ++;
                    }
                }
            }
            if(cnt != k){
                if(index1 == t1.size()){
                    while(cnt < k){
                        result.pb(t2[index2]);
                        cnt++;
                        index2++;
                    }
                }else{
                    while(cnt< k){
                        cnt++;
                        result.pb(t1[index1]);
                        index1++;
                    }
                }
            }
            if(compare(result,0,tmp,0)){
                for (int j = 0; j < k; ++j) {
                    tmp[j] = result[j];
                }
            }
        }
        return tmp;
    }
};
int main() {
    printf("hello ");
    Solution h;
    /*
     * [8,0,4,4,1,7,3,6,5,9,3,6,6,0,2,5,1,7,7,7,8,7,1,4,4,5,4,8,7,6,2,2,9,4,7,5,6,2,2,8,4,6,0,4,7,8,9,1,7,0]
[6,9,8,1,1,5,7,3,1,3,3,4,9,2,8,0,6,9,3,3,7,8,3,4,2,4,7,4,5,7,7,2,5,6,3,6,7,0,3,5,3,2,8,1,6,6,1,0,8,4]
50
     * */

    vi s = {8,0,4,4,1,7,3,6,5,9,3,6,6,0,2,5,1,7,7,7,8,7,1,4,4,5,4,8,7,6,2,2,9,4,7,5,6,2,2,8,4,6,0,4,7,8,9,1,7,0};
    vi ss = {6,9,8,1,1,5,7,3,1,3,3,4,9,2,8,0,6,9,3,3,7,8,3,4,2,4,7,4,5,7,7,2,5,6,3,6,7,0,3,5,3,2,8,1,6,6,1,0,8,4};
    int k = 50;
    cout<<s.size()<<ss.size()<<endl;
    h.maxNumber(s,ss,k);
//    vi result = h.maxNumber(s,ss,k);
//    out(result.begin(),result.end());

}