#include <iostream>
#include <string>

// A Basic Implementation of a proleptic Gregorian Calendar in C++

class Date{
    private:
        int month, day, year, julianDay;
        std::string days[7] = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
        std::string months[12] = {
            "January", "February", "March", "April", "May", 
            "June", "July"," August", "September", "October", 
            "November", "December"
        };
        int months_30[4] = {4, 6, 9, 11};
        int months_31[7] = {1, 3, 5, 7, 8, 10, 12};
        // std::string something = {"Me", "You"};

        // std::string switchName(int num, std::string *arr) {
        //     int i;
        //     std::string name;
        //     switch (i) {
        //         for (i=0; i<num; i++) {
        //             case i:
        //                 name = arr[i];
        //                 break;
        //         }
        //     }
        // }

        int * toGregorian() {
            static int dateArr[3];
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
            dateArr[0] = month;
            dateArr[1] = day;
            dateArr[2] = year;
            return dateArr;
        }

    public:

        int getDay();
        int getMonth();
        int getYear();
        int dayOfWeek();
        std::string dayName();
        std::string monthName();
        int firstDayOfMonth();
        std::string firstDayOfMonthName();
        bool isLeapYear();

        void show();
        void getNumberOfDaysInMonth();

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
    int *dateArr;
    dateArr = toGregorian();
    int month, day, year;
    month = dateArr[0];
    day = dateArr[1];
    year = dateArr[2];

    if (month < 3) {
        month = month + 12;
        year = year - 1;
    }
    return ((13 * month + 3) / 5 + day + year + year / 4 - year / 100 + year / 400) % 7;
}

std::string Date::dayName() {
    return days[dayOfWeek()];
}

std::string Date::monthName() {
    return months[getMonth() - 1];
}

bool Date::isLeapYear() {
    if (year % 4 == 0) {
        if (year % 100 == 0) {
            if (year % 400 == 0) {
                return true;
            }else {
                return false;
            }
        }else {
            return true;
        }
    }else {
        return false;
    }
}

int Date::firstDayOfMonth() {
    int daysArr[7] = {0, 1, 2, 3, 4, 5, 6};
    int dayNum = getDay() % 7;
    day = daysArr[dayOfWeek() - (dayNum - 1)];
    return day;
}

std::string Date::firstDayOfMonthName() {
    day = firstDayOfMonth();
    return months[day];
}

void Date::getNumberOfDaysInMonth() {
    
}