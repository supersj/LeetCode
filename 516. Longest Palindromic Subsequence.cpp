
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
    int longestPalindromeSubseq(string s) {

        int sl = int(s.size());
        if (sl == 0) return 0;
        int p[sl][sl] = {0};
        for (int j = 0; j < sl; ++j) {
            p[j][j] = 1;
        }
        for (int k = 2; k <= sl ; ++k) {
            for (int i = 0; i < sl - k + 1; ++i) {
                p[i][i+k-1] = (s[i]==s[i+k-1] ? p[i+1][i+k-2] + 2:max(p[i+1][i+k-1],p[i][i+k-2]));
            }
        }
        return p[0][sl-1];
    }
};

int main() {
    printf("hello ");
    Solution h;
    vi c = {1,2};
    vector<pair<int, int>> e;
    e.pb(mp(2,2));
    e.pb(mp(0,3));
    e.pb(mp(1,5));
    string heihei ("bbbab");

    int amount = 5;
    int s = h.longestPalindromeSubseq(heihei);
    cout<<s;
}