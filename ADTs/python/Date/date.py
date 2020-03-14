# Implements a proleptic Gregorian calendar date as a Julian day number
from datetime import date


class Date:

    # Creates an object instance for the specified Gregorian date.
    # Methods to be implemented:
    # 1. month() - Returns the month of the date
    # 2. day() - Returns the day of the date
    # 3. year() - Returns the year of the date
    # 4. dayOfWeek() - Returns the day of the week of the date, 0 - Monday, 1 - Tuesday, etc
    # 5. toString() - Returns the string representation of the date Example '02/05/2008'
    # 6. greaterThan(other_date) - Compares date to check whether its greater than
    # 7. lessThan(other_date) - Compares date to check whether its less than
    # 8. lessThanOrEqualTo(other_date) - Compares date to check whether its less than or equal to

    def __init__(self, month=0, day=0, year=0):
        # Keep Date Object Reference
        mDate = date
        if month == 0 & day == 0 & year == 0:
            today = mDate.today()
            month = today.month
            day = today.day
            year = today.year

        self._julianDay = 0
        self._days_in_words = {
            0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
            4: 'Friday', 5: 'Saturday', 6: 'Sunday'
        }
        self._days_in_order = {
            0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
            4: 'Thursday', 5: 'Friday', 6: 'Saturday'
        }
        self._months_in_words = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
            6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October',
            11: 'November', 12: 'December'
        }

        self._months_30 = {4, 6, 9, 11}
        self._months_31 = {1, 3, 5, 7, 8, 10, 12}

        assert self._isValidGregorian(month, day, year), \
            "Invalid Gregorian date."

        # The first line of the equation, T = (M -14) / 12 has to be changed
        # since Python's implementation of integer division is not the same
        # as the mathematical definition
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + \
                          (367 * (month - 2 - tmp * 12) // 12) - \
                          (3 * ((year + 4900 + tmp) // 100) // 4)

    def month(self):
        return (self._toGregorian())[0]

    def day(self):
        return (self._toGregorian())[1]

    def year(self):
        return (self._toGregorian())[2]

    def dayOfWeek(self):
        month, day, year = self._toGregorian()
        if month < 3:
            month = month + 12
            year = year - 1
        return ((13 * month + 3) // 5 + day + \
                year + year // 4 - year // 100 + year // 400) % 7

    def dayOfWeekInWords(self):
        day_num = self.dayOfWeek()
        return self._days_in_words[day_num]

    def monthInWords(self):
        month_num = self.month()
        return self._months_in_words[month_num]

    def firstDayOfMonth(self):
        daysList = (0, 1, 2, 3, 4, 5, 6)
        dayNum = (self.day()) % 7
        day = daysList[self.dayOfWeek() - (dayNum-1)]

        return day

    def firstDayOfMonthInWords(self):
        day = self.firstDayOfMonth()
        return self._days_in_words[day]

    def getNumberOfDaysInMonth(self):
        month_number = -1

        if self.month() in self._months_30:
            month_number = 30
        elif self.month() in self._months_31:
            month_number = 31
        elif self.month() == 2:
            if self.isLeapYear(self.year()):
                month_number = 29
            else:
                month_number = 28

        return month_number

    def printCalendar(self):
        
        # Print Days Abbreviations 
        daysAbbrev = "Su Mo Tu We Th Fr Sa"
        month_year = self.monthInWords() + " " + str(self.year())
        spaces = int((len(daysAbbrev) - len(month_year))/2)
        print(" "*spaces+"{month_year}".format(month_year=month_year))
        print(daysAbbrev)
        calendar_days = {
            0: "Su", 1: "Mo", 2: "Tu", 3: "We",
            4: "Th", 5: "Fr", 6: "Sa"
        }
        month_number = self.getNumberOfDaysInMonth()
        firstDay = self.firstDayOfMonth() + 1
       
        # Print The Date (Days) In Order
        for day in range(month_number+firstDay):
            end = ''
            if (day+1) % 7 == 0:
                end = '\n'
            if (firstDay) > 0:
                print("   ", end=end)
                firstDay -= 1
                day -= 1
            else:
                mDay = day-self.firstDayOfMonth()
                print("%02d " % (day-self.firstDayOfMonth()), end=end)

        print()


    def __str__(self):
        month, day, year = self._toGregorian()
        return "%02d/%02d/%04d" % (month, day, year)

    def __eq__(self, other_date):
        return self._julianDay == other_date._julianDay

    def __lt__(self, other_date):
        return self._julianDay < other_date._julianDay

    def __le__(self, other_date):
        return self._julianDay <= other_date._julianDay

    def __gt__(self, other_date):
        return self._julianDay >= other_date._julianDay

    def __ge__(self, other_date):
        return self._julianDay > other_date._julianDay

    def isLeapYear(self, year=None):
        if year is None:
            year = self.year()
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def _toGregorian(self):
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month // 80)
        A = month // 11
        month = month + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year

    def _isValidGregorian(self, month, day, year):
        if month in self._months_30:
            if (day > 0) & (day <= 30):
                return True
            else:
                return False
        elif month in self._months_31:
            if (day > 0) & (day <= 31):
                return True
            else:
                return False
        elif month == 2:
            if self.isLeapYear(year):
                if (day > 0) & (day <= 29):
                    return True
                else:
                    return False
            elif not self.isLeapYear():
                if (day > 0) & (day <= 28):
                    return True
                else:
                    return False


if __name__ == "__main__":
    import pdb; pdb.set_trace()
