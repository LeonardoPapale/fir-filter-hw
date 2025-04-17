//This script is a generic implementation of a FIR filter in C
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <vector>
#include <iostream>

#define FILTER_LENGTH 100
double coefficients[FILTER_LENGTH] = {0};
double circular_buffer[FILTER_LENGTH] = {0};

std::vector<float> generateVector()
{
    return {0.0f, 1.5f, 6.03f, 3.4f, 1.0f};
}

void printVector(const std::vector<float>& vec) {
    for (float val : vec) {
        std::cout << val << " ";
    }
    std::cout << std::endl;
}

int main(void)
{
    //import the data from csv file, it will be the ADC 
    // double new_sample = import_from_csv();
    std::vector<float> array = generateVector();
    printVector(array);
  
    
    //double fir_filter_output = fir_filter(new_sample);
    //export the data to csv file, it will be sent to DAC
    return 0;
}



