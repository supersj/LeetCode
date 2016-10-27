#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    string s;
    string s1 = "asd";
    string s2 = "asdasdas";

    int p[10] = {0};
    for (int i = 0; i < 10; ++i)
    {
        cout << p[i] << endl;
    }
    s = s1 + s2;
    cout << s << endl;
    return 0;
}