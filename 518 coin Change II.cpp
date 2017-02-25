
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
    int helper(int amount, vector<int>& coins,int start,int end,vi coinstack,int **dp) {
        if(amount < 0){
            return 0;
        }
        if (amount == 0){
            return 1;
        }
        if (dp[amount-1][start] != -1){
            return dp[amount-1][start];
        }
        int inc = 0;
        int ninc = 0;
        coinstack.pb(coins[start]);
        amount -= coins[start];
        inc = helper(amount,coins,start,end,coinstack,dp);
        coinstack.pop_back();
        amount += coins[start];
        if(start + 1 < end) {
            ninc = helper(amount, coins, start + 1, end, coinstack,dp);
        }
        dp[amount-1][start] = inc + ninc;
        return inc + ninc;
    }
    int change(int amount, vector<int>& coins) {
        if(amount == 0){
            return 1;
        }
        if(coins.size() == 0){
            return 0;
        }
        int start = 0;
        int end = int(coins.size());
        sort(coins.rbegin(),coins.rend());
        vi coinstack;
        int **dp;
        dp=new int*[amount];
        for(int i=0;i<amount;i++)
        {
            dp[i]=new int[coins.size()];
        }
        for (int j = 0; j < amount; ++j) {
            for (int i = 0; i < coins.size(); ++i) {
                dp[j][i] = -1;
            }
        }
        int result = helper(amount,coins,start,end,coinstack,dp);
        for (int k = 0; k < amount; ++k) {
            delete dp[k];
        }
        delete dp;
        return result;
    }
};
int main() {
    printf("hello ");
    Solution h;
    vi c = {1,2};
    int amount = 5;
    cout<<h.change(amount,c);
}