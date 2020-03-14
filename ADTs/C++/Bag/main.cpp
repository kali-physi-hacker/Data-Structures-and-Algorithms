#include <iostream>
#include "Bag.hpp"

int main() {
    Bag bag;
    std::cout << "An Basic Implementation of the Bag ADT\n";
    bag.add(7);
    bag.add(9);
    // bag.remove(9);
    bag.add(12);
    std::cout << "This is bag experiments " << bag[3];  
    return 0;
}