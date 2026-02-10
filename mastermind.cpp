#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;

int main() {
    srand(time(nullptr));

    int hiddennum[4];
    for (int &element : hiddennum) {
        element = rand() % 10; 
        cout << element << " ";
    }

    return 0;
}
