#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>
using namespace std;

int main() {
    srand(time(nullptr));

    int hiddennum[4];
    for (int &element : hiddennum) {
        element = rand() % 10;
    }

    const int MAX_GUESSES = 8;
    bool won = false;

    cout << "Welcome to Mastermind!" << endl;
    cout << "Guess the 4-digit number. Each digit is 0-9." << endl;
    cout << "A = correct digit, correct position" << endl;
    cout << "B = correct digit, wrong position" << endl << endl;

    for (int i = 0; i < MAX_GUESSES; i++) {
        int x;
        cout << "Guess " << (i + 1) << "/" << MAX_GUESSES << " - Enter a 4-digit number: ";
        cin >> x;

        // Parse digits (d is leftmost, a is rightmost)
        int guess[4];
        guess[3] = x % 10; x /= 10;
        guess[2] = x % 10; x /= 10;
        guess[1] = x % 10; x /= 10;
        guess[0] = x % 10;

        // Count A's (correct digit, correct position)
        int countA = 0, countB = 0;
        bool hiddenUsed[4] = {false, false, false, false};
        bool guessUsed[4]  = {false, false, false, false};

        for (int j = 0; j < 4; j++) {
            if (guess[j] == hiddennum[j]) {
                countA++;
                hiddenUsed[j] = true;
                guessUsed[j]  = true;
            }
        }

        // Count B's (correct digit, wrong position)
        for (int j = 0; j < 4; j++) {
            if (guessUsed[j]) continue;
            for (int k = 0; k < 4; k++) {
                if (hiddenUsed[k]) continue;
                if (guess[j] == hiddennum[k]) {
                    countB++;
                    hiddenUsed[k] = true;
                    break;
                }
            }
        }

        string result = "";
        for (int j = 0; j < countA; j++) result += 'A';
        for (int j = 0; j < countB; j++) result += 'B';

        cout << "Result: " << (result.empty() ? "No matches" : result) << endl << endl;

        if (countA == 4) {
            won = true;
            cout << "Congratulations! You guessed the number in " << (i + 1) << " guess(es)!" << endl;
            break;
        }
    }

    if (!won) {
        cout << "Game over! The hidden number was: ";
        for (int i = 0; i < 4; i++) cout << hiddennum[i];
        cout << endl;
    }

    return 0;
}