
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
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        int index_1 = 0,index_2 = 0;
        int len1 = int(nums1.size());
        int len2 = int(nums2.size());
        int is1 = 0;
        vector<int> result;
        int i1 = 0,i2 = 0,e1 = len1,e2 = len2,l1 = 0,l2 = 0,t1 = 0,t2 = 0;
        while(k > 0){
            k--;
            int curmax1 = 0;
            int curmax2 = 0;
            int curmax = 0;
            int remain = len1 - l1 + len2 - l2 - k;
            if(t1 >= len1){
                k++;
                while(k>0){
                    k--;
                    remain = len2 - k  ;
                    curmax = 0;
                    for (int ii = l2; ii < min(remain,len2); ++ii) {
                        if(nums2[ii] > curmax){
                            curmax = nums2[ii];
                            l2 = ii;
                        }
                    }
                    l2 ++;
                    result.push_back(curmax);
                }
                break;
            }
            if(t2 >= len2){
                k++;
                while(k>0){
                    k--;
                    remain = len1 - k;
                    curmax = 0;
                    for (int ii = l1; ii < min(remain,len1); ++ii) {
                        if(nums1[ii] > curmax){
                            curmax = nums1[ii];
                            l1 = ii;
                        }
                    }
                    l1 ++;
                    result.push_back(curmax);
                }
                break;
            }
            for(i1 = l1;i1 < min(l1+remain,len1);i1++){
                if(nums1[i1] > curmax1){
                    curmax1 = nums1[i1];
                    t1 = i1;
                }
            }
            for(i2 = l2;i2 <min(l2+remain,len2);i2++){
                if(nums2[i2] > curmax2){
                    curmax2 = nums2[i2];
                    t2 = i2;
                }
            }
            if(nums1[t1] > nums2[t2] ){
                l1 = t1 + 1;
                t1++;
            } else if(nums1[t1] == nums2[t2]){
                int t = 0;
                int isbreak = 0;
                for(t = 1; t <= t1-l1 && t <=t2-l2; t ++) {
                    if (nums1[t1 - t] != nums2[t2 - t]) {
                        is1 = nums1[t1 - t] > nums2[t2 - t]?0:1;
                        isbreak = 1;
                        break;
                    }
                }

                if(!isbreak && (t == t1-l1 || t == t2-l2)){
                    if(t == t1-l1){
                        is1 = 1;
                    }else{
                        is1 = 0;
                    }
                }
                if(is1 == 1){
                    l1 = t1+1;
                    t1++;
                }else{
                    l2 = t2+1;
                    t2++;
                }
            }else{
                l2 = t2 + 1;
                t2++;
            }

            result.push_back(max(curmax1,curmax2));
        }
        return result;
    }
};
int main() {
    printf("hello ");
    Solution h;
    /*
     * [3,4,6,5]
    [9,1,2,5,8,3]
    5
     * */
    vi s = {3,4,6,5};
    vi ss = {9,1,2,5,8,3};
    int k = 5;
    vi result = h.maxNumber(s,ss,k);
    out(result.begin(),result.end());

}