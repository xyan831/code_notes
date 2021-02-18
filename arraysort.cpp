#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "arraysort.h"

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

void randarray(int size, int min, int max, int rarray[])
{
	int i;
	time_t t;
	
	srand((unsigned) time(&t));

	for (i=0; i<size; i++)
	{
		rarray[i] = (rand()%(max+1-min))+min;
	}

	printf("\nRandom number array:\n");
	for (i=0; i<size; i++)
	{
		printf("%d\t", rarray[i]);
	}
}

void sortarray(int size, int rarray[], int sarray[])
{
	int i, j, a;
	for (i=0; i<size; i++)
	{
		sarray[i] = rarray[i];
	}
	for (i=0; i<size; i++)
	{
		for (j=i+1; j<size; j++)
		{
			if (sarray[i]>sarray[j])
			{
				a = sarray[i];
				sarray[i] = sarray[j];
				sarray[j] = a;
			}
		}
	}
	printf("\nSorted number array:\n");
	for (i=0; i<size; i++)
	{
		printf("%d\t", sarray[i]);
	}
}