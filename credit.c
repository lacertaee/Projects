#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number;
    //prompt user for number
    number = get_long("Number: ");
    //get first digit if number has 16 digits
    long one = number / 1000000000000000;
    //get first two digit if number has 16 digits
    long two = number / 100000000000000;
    //get first two digit if nummber has 15 digits
    long one1 = number / 10000000000000;
    //get first digit if number has 13 digits
    long one2 = number / 1000000000000;
    long n = 0;
    long total = 0;
    long count = 0;
    long even = 0;
    long odd = 0;
    //calculate checksum.
    while (number != 0)
    {
        n = number % 10;
        total += n;
        number /= 10;
        count++;
        if (count % 2 == 0)
        {
            long h = 0;
            long b = 0;
            long k = n * 2;
            long e = 0;
            //get even number
            if (k >= 10)
            {
                b = k % 10;
                e = k / 10;
                h = b + e;
                even += h;
            }
            else
            {
                even += n * 2;
            }
        }
        else
        {
            //get odd number
            odd += n;
        }
    }
    int all = odd + even;
    //check if users card is legit and if it is, print american express,
    //visa or mastercard
    if (all % 10 == 0)
    {
        if ((count == 15 && one1 == 34) || (count == 15 && one1 == 37))
        {
            printf("AMEX\n");
        }
        else if ((count == 13 && one2 == 4) || (count == 16 && one == 4))
        {
            printf("VISA\n");
        }
        else if ((count == 16 && two == 51) || (count == 16 && two == 52)
                 || (count == 16 && two == 53) || (count == 16 && two == 54)
                 || (count == 16 && two == 55))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}