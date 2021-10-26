#include <stdio.h>
void main(){
    float x, y, z;
    print("Enter the pool's x:");
    scanf_s("%f", &x);
    print("Enter the pool's y:");
    scanf_s("%f", &y);
    print("Enter the pool's z:");
    scanf_s("%f", &z);

    print("pool's volume is %f",(x*y*z));
}