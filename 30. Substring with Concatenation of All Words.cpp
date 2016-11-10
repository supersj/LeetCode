#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        unordered_map<string, int> counts;
        for (string word : words)
            counts[word]++;
        int n = s.length(), num = words.size(), len = words[0].length();
        vector<int> indexes;
        for (int i = 0; i < n - num * len + 1; i++) {
            unordered_map<string, int> seen;
            int j = 0;
            for (; j < num; j++) {
                string word = s.substr(i + j * len, len);
                if (counts.find(word) != counts.end()) {
                    seen[word]++;
                    if (seen[word] > counts[word])
                        break;
                }
                else break;
            }
            if (j == num) indexes.push_back(i);
        }
        return indexes;
    }
};


// travel all the words combinations to maintain a window
// there are wl(word len) times travel
// each time, n/wl words, mostly 2 times travel for each word
// one left side of the window, the other right side of the window
// so, time complexity O(wl * 2 * N/wl) = O(2N)
vector<int> findSubstring(string S, vector<string> &L) {
    vector<int> ans;
    int n = S.size(), cnt = L.size();
    if (n <= 0 || cnt <= 0) return ans;

    // init word occurence
    unordered_map<string, int> dict;
    for (int i = 0; i < cnt; ++i) dict[L[i]]++;

    // travel all sub string combinations
    int wl = L[0].size();
    for (int i = 0; i < wl; ++i) {
        int left = i, count = 0;
        unordered_map<string, int> tdict;
        for (int j = i; j <= n - wl; j += wl) {
            string str = S.substr(j, wl);
            // a valid word, accumulate results
            if (dict.count(str)) {
                tdict[str]++;
                if (tdict[str] <= dict[str])
                    count++;
                else {
                    // a more word, advance the window left side possiablly
                    while (tdict[str] > dict[str]) {
                        string str1 = S.substr(left, wl);
                        tdict[str1]--;
                        if (tdict[str1] < dict[str1]) count--;
                        left += wl;
                    }
                }
                // come to a result
                if (count == cnt) {
                    ans.push_back(left);
                    // advance one word
                    tdict[S.substr(left, wl)]--;
                    count--;
                    left += wl;
                }
            }
            // not a valid word, reset all vars
            else {
                tdict.clear();
                count = 0;
                left = j + wl;
            }
        }
    }

    return ans;
}
void print() {
    unordered_map<string, int> wordmap;
    wordmap["123"]++;
    wordmap["143"]++;
    wordmap["543"]++;
    for (unordered_map<string, int>::iterator i = wordmap.begin(); i != wordmap.end(); ++i)
    {
        cout << i->first << " " << i->second << endl;
    }
}


int main(int argc, char const *argv[])
{
    print();
    return 0;
}