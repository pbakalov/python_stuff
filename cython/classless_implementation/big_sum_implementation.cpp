#include <cmath>
#include "big_sum_implementation.h"

void big_calculation(double* data, int size) {
    for (int j = 0; j<10000; j++) {
        for (int i = 0; i<size; i++) {
            data[i] = pow((i+1.),2);
            //data[i] = (i+1.);
        }
    }
}
