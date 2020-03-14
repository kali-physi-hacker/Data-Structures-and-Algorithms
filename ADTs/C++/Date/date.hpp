#include <iostream>
#include <string>

// A Basic Implementation of a proleptic Gregorian Calendar in C++

class Date{
    private:
        int month, day, year, julianDay;
        int toGregorian() {
            int A = julianDay + 68569;
            int B = 4 * A / 146097;
            A = A - (146097 * B + 3) / 4;
            year = 4000 * (A + 1) / 1461001;
            A = A - (1461 * year / 4) + 31;
            month = 80 * A / 2447;
            int day = A - (2447 * month / 80);
            A = month / 11;
            month = month + 2 - (12 * A);
            year = 100 * (B - 49) + year + A;
            return month, day, year;
        }

    public:

        int getDay();
        int getMonth();
        int getYear();
        int dayOfWeek();

        void show();

        Date(int Mmonth=0, int mDay=0, int mYear=0) {
            julianDay = 0;
            month = Mmonth;
            day = mDay;
            year = mYear;

            int tmp = 0;
            if (month < 3) {
                tmp = -1;
            }
            julianDay = day - 32075 + (1461 * (year + 4800 + tmp) / 4) + (367 * (month - 2 - tmp * 12) / 12) - (3 * ((year + 4900 + tmp) / 100) / 4);

        }
    
};


int Date::getDay() {
    return day;
}

int Date::getMonth() {
    return month;
}

int Date::getYear() {
    return year;
}

void Date::show() {
    std::string date = std::to_string(month) + "/" + std::to_string(day) + "/" + std::to_string(year);
    std::cout << date << '\n';
}

int Date::dayOfWeek() {
    month, day, year = toGregorian();
    if (month < 3) {
        month = month + 12;
        year = year - 1;
    }
    return ((13 * month + 3) / 5 + day + year + year / 4 - year / 100 + year / 400) % 7;
}