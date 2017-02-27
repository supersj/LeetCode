
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
    bool isin(pair<int,int>small,pair<int,int>big){
        if(small.second < big.second) return true;
        return false;
    }
    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        if(envelopes.size() == 0){
            return 0;
        }
        int maxist = INT32_MIN;
        sort(envelopes.begin(),envelopes.end());
        vi result(envelopes.size(),1);
        for(int i = 0;i<envelopes.size();i++){
            for (int j = i-1; j >= 0 ; --j) {
                if (isin(envelopes[j],envelopes[i])){
                    result[i] = result[j]+1;
                    break;
                }
            }
            maxist = max(maxist,result[i]);
        }
        return maxist;
    }
};

