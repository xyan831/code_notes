#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include "basecon.h"	/* dec_xxx, dec_convert */
#include "arraysort.h"	/* minmax, multiple, randarray, sortarray */

/*
#pragma pack(1)

typedef struct {
    unsigned char m;
    unsigned char n;
} _Q;

typedef union {
     unsigned short a;
     _Q				b;
 } _W;
*/

int main(void)
{
	int n;
	char convert1[100], convert2[100], convert3[100];
	int a[] = {2, 46, 5, 8, 235, 75, 3, 8, 22, 4};
	int min, max;
	int rarray[10], sarray[10];
	
/*
	_W w;
	printf("\n%d bytes: a", sizeof(w.a));
	printf("\n%d bytes: m", sizeof(w.b.m));
	printf("\n%d bytes: n", sizeof(w.b.n));

	w.a = 255;
	printf("\nm = %d, n = %d", w.b.m, w.b.n);

	w.b.m = 0;
	w.b.n = 0;
	printf("\na = %d", w.a);
*/

	// clear command prompt
//	system("cls");

	// print "very good"
	printf("**********************************\n");
	printf("         V e r y  g o o d !       \n");
	printf("**********************************\n");

	// decimal to octal, hexadecimal
//	printf("\nInput Decimal to Convert: ");
//	scanf("%d", &n);
	n = 218;
	dec_xxx(n);

	// decimal to base 2, 8, 16
//	printf("\nInput Decimal to Convert: ");
//	scanf("%d", &n);
	n = 218;
	dec_convert(n, 2, convert1);
	dec_convert(n, 8, convert2);
	dec_convert(n, 16, convert3);

	// find minmax of number array
	minmax(a, sizeof(a)/sizeof(a[0]), &min, &max);
	printf("min = %d, max = %d\n", min, max);

	// find multiple of number from range
	multiple(9, 1, 100);

	// create random number array
	randarray(10, 0, 50, &rarray[0]);
	// sort the random number array in ascending order
	sortarray(10, &rarray[0], &sarray[0]);

	return 0;
}