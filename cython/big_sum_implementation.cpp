#include <cmath>
#include "big_sum_implementation.h"
using namespace std;

void myclass::big_calculation(double* data, int size) {
    for (int i = 0; i<size; i++) {
        data[i] = pow((i+1.),10);
    }
}
