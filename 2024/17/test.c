#include<stdio.h>
#include <math.h>

long pow2(int n) {
    return (long) 1 << n;
}

int main() {

	long int A = 1000;
	while (A != 0){
	    long int out  = ((((A % 8) ^ 5) ^ 6) ^ ((A / (pow2((A % 8))))) % 8);
	    printf("%ld\n", out);
	    A = (A / pow2(((A % 8) ^ 5) ^ 6));

	}
	return 0;
}