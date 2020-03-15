#include <iostream>
#include "date.hpp"

using namespace std;


int main() {
    Date date;
    date = Date(3,3,2020);
    date.show();
    std::cout << "The day of the week: " << date.dayOfWeek() << '\n';
    std::cout << "The day of the week in words is: " << date.dayName() << '\n';
    std::cout << "The month name is also: " << date.monthName() << '\n';

    if (date.isLeapYear()) {
        std::cout << "The year is a leap year\n";
    }else {
        std::cout << "The year is not a leap year\n";
    }
    return 0;
}