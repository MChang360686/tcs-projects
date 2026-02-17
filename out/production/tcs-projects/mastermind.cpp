#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main() {
    srand(time(nullptr));

    int hiddennum[4];
    for (int &element : hiddennum) {
        element = rand() % 10; 
        
    }
    
    int x, a, b, c, d;
    string result = "";
    for (int i = 0; i < 8; i++) {
        cout << "Enter a 4 digit number: ";
        cin >> x;
        a = x % 10;
        x /= 10;
        b = x % 10;
        x /= 10;
        c = x % 10;
        x /= 10;
        d = x % 10;
        
        cout << a << b << c << d << "\n";
        
        if (0[hiddennum] == d) {
            result += 'A';
        }
        
        
    }

    return 0;
}
