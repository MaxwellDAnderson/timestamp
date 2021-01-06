#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
//#include <iomanip>
//#include <istream>
#include <ctime>

using namespace std;


int main() {

    time_t now;
    struct tm *current;
    now = time(0);
    current = localtime(&now);
    string stamp = asctime(current);
    stamp.pop_back();
    cout << stamp << ": ";

    string endDocument = "\\\\\\";
    string userInput;


    while (!(cin >> userInput) || (userInput != endDocument)) {
        now = time(0);
        current = localtime(&now);
        string stamp = asctime(current);
        stamp.pop_back();
        cout << stamp << ": ";
        cin.ignore(256, '\n');
    }


    now = time(0);
    current = localtime(&now);
    string finalStamp = asctime(current);
    finalStamp.pop_back();
    cout << finalStamp << ": ";
    cin.ignore(256, '\n');
    cout << "---END OF DOCUMENT---";

}
