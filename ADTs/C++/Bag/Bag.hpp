#include <iostream>

using namespace std;


class Bag{
    // private int[] theItems = {0};
    public:
        int size;
        int length();
        void add(int element);
        void remove(int element);
        int *theItems;

        int &operator[](int index) {
            if (index >= size) {
                cout << '\n\n' << "Bag index out of bound, exiting\n";
                exit(0);
            }
            return theItems[index];
        }

        Bag() {
            size = 1;
            theItems = new int(1);
            theItems[0] = 0;
        }

};

// Returns the length of the Bag ADT
int Bag::length() {
    return size;
}


// Adds an element to the Bag
void Bag::add(int element) {
    int oldItems[size];
    for (int i=0; i<size; i++) {
        oldItems[i] = theItems[i];
    }

    theItems = new int[size + 1];
    for (int i=0; i<size; i++) {
        theItems[i] = oldItems[i];
    }
    
    theItems[size] = element;
    size += 1;
}

void Bag::remove(int element) {
    int oldItems[size];
    for (int i=0; i<size; i++) {
        oldItems[i] = theItems[i];
    }

    theItems = new int[size - 1];
    for (int i=0; i<size-1; i++) {
        theItems[i] = oldItems[i];
    }
    size -= 1;
}
