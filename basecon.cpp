#include <stdio.h>
#include "basecon.h"

void dec_xxx(int n)
{
	printf("\nOctal Number for %d = %o", n, n);
	printf("\nHexadecimal Number for %d = %X", n, n);
}

void dec_convert(int n, int r)
{
	int i=1, j, temp;
	char hexadecimalNumber[100];
	
	printf("\nBase %d Number for %d = ", r, n);
	
	while (n!=0)
	{
		temp = n%r;

		//To convert integer into character
		if (temp < 10)
		{
			temp = temp + 48;
		}
		else
		{
			temp = temp + 55;
		}
		
		hexadecimalNumber[i++]= temp;
		n = n/r;
	}
	
	for (j=i-1; j>0; j--)
	{
		printf("%c",hexadecimalNumber[j]);
	}
}
