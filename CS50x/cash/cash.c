#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int change;
    int coins;
    do
    {
        change = get_int("Change owed: ");
    }
    while (change < 1);

    int q = change / 25;
    int d = (change % 25) / 10;
    int n = ((change % 25) % 10) / 5;
    int p = (((change % 25) % 10) % 5);

    coins = q + d + n + p;

    printf("%i\n", coins);
}
