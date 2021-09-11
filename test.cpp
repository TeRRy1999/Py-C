#include <iostream>
using namespace std;



extern "C" int* ls1(int *input){
    for (int i = 0; i < 64000000; ++i)
    {
        input[i]+=2;
    }
    return input; 
}

extern "C" int** ls2(){
    int** information = new int*[3];
    int count = 0;
    for (int i = 0; i < 3; ++i)
    {
        information[i] = new int[3];
    }
    for(int k=0;k<3;k++){
        for(int j=0;j<3;j++)
            information[k][j] = count++;
    }
    return information;
}
