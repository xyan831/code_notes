#include <stdio.h>
#include <stdlib.h>
#include "basecon.h"

void minmax(int a[], int len, int *min, int *max);
void multiple(int fac, int start, int end);

int main(void)
{
//	int a[] = {1, 2, 3};
//	int min, max;
	int n;
	
	// clear command prompt
//	system("cls");

	// print "very good"
	printf("**********************************\n");
	printf("         V e r y  g o o d !       \n");
	printf("**********************************\n");

	// find minmax of number array
/*	minmax(a, sizeof(a)/sizeof(a[0]), &min, &max);
	printf("min = %d, max = %d\n", min, max);
*/
	// find multiple of number from range
	multiple(9, 1, 100);

	// decimal to octal, hexadecimal
//	printf("\nInput Decimal to Convert: ");
//	scanf("%d", &n);
	n = 501;
	dec_xxx(n);

	// decimal to base 2, 8, 16
//	printf("\nInput Decimal to Convert: ");
//	scanf("%d", &n);
	n = 218;
	dec_convert(n, 2);
	dec_convert(n, 8);
	dec_convert(n, 16);

	return 0;
}

void minmax(int a[], int len, int *min, int *max)
{
	int i;

/*	printf("type integer: ");
	scanf("%d", &a[0]);
	printf("type integer: ");
	scanf("%d", &a[1]);
	printf("type integer: ");
	scanf("%d", &a[2]);
*/
	*min = *max = a[0];
	for (i=1; i<len; i++) {
		if (a[i] < *min) {
			*min = a[i];
		}
		if (a[i] > *max) {
			*max = a[i];
		}
	}
}

void multiple(int fac, int start, int end)
{
	int i;

	printf("Multiples of %d in range %d - %d:\n", fac, start, end);
	for (i=start; i<(end+1); i++)
	{
		if (i%fac == 0)
		{
			printf("%d ", i);
		}
	}
}
