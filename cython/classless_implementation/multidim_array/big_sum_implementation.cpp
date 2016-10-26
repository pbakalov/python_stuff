#include <cmath>
#include "big_sum_implementation.h"

void big_calculation(double* data, int size, int size2, int size3) {
    for (int j = 0; j<1000; j++) {
        for (int i = 0; i<size; i++) {
            for (int k = 0; k<size2; k++) {
                for (int l = 0; l<size3; l++) {
                    data[i*(size2*size3)+k*size3 + l] = pow((i+1.)*(k+1.)*(l+1.),2);
                }
            }
        }
    }
}
