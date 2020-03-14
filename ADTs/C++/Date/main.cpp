#include <iostream>
#include "date.hpp"

using namespace std;


int main() {
    Date date;
    date = Date(3,3,2020);
    date.show();
    date.dayOfWeek();
    return 0;
}