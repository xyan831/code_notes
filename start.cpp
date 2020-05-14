#include <stdio.h>
#include <stdlib.h>

void minmax(int a[], int len, int *min, int *max);
void nine();
void dec_bin();
void dec_oct();
void dec_hex();

int main(void)
{
	int a[] = {1, 2, 3};
	int min, max;
	
	// clear command prompt
//	system("cls");

	// 1) print goodjob
	printf("**********************************\n");
	printf("         V e r y  g o o d !       \n");
	printf("**********************************\n");

	// 2) find minmax of number array
	minmax(a, sizeof(a)/sizeof(a[0]), &min, &max);
	printf("min = %d, max = %d\n", min, max);

	// 3) find multiple of 9 from 1-100
//	nine();

	// 4) decimal to binary
	dec_bin();

	// 5) decimal to octal
	dec_oct();

	// 6) decimal to hexadecimal
	dec_hex();

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

void nine()
{
//	int i;
//	int b[10];
	
/*	for (i=1, i<11, ++i)
	{
		printf("%d\n", i);
	}
*/
}

void dec_bin()
{
	int b[10], n, i;
	
	// enter decimal or use default
//	printf("\nEnter decimal to convert: ");
//	scanf("%d", &n);
	n = 13;
	
	for(i=0; n>0; i++)
	{
		b[i] = n%2;
		n = n/2;
	}

	printf("\nBinary Number: ");

	for(i=i-1; i>=0; i--)
	{
		printf("%d", b[i]);
	}
}

void dec_oct()
{
	int o[10], n, i;
	
	// enter decimal or use default
//	printf("\nEnter decimal to convert: ");
//	scanf("%d", &n);
	n = 210;
	
	for(i=0; n>0; i++)
	{
		o[i] = n%8;
		n = n/8;
	}

	printf("\nOctal Number: ");

	for(i=i-1; i>=0; i--)
	{
		printf("%d", o[i]);
	}
}

void dec_hex()
{
	long int n;

	// enter decimal or use default
//	printf("\nEnter decimal to convert: ");
//	scanf("%ld",&n);
	n = 501;

	printf("\nHexadecimal Number: %X", n);
}
