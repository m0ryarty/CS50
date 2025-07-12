#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    if (argc != 2 || argc > 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (argv[1][i] < '0' || argv[1][i] > '9')
        {
            printf("Usage: %s key\n", argv[0]);
            return 1;
        }
    }

    int key = 0;

    if (atoi(argv[1]) > 26)
    {
        key = atoi(argv[1]) % 26;
    }
    else
    {
        key = atoi(argv[1]);
    }

    int cipher;
    int ascii;

    string plaintext = get_string("plaintext:  ");

    printf("ciphertext: ");

    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {

        if (tolower(plaintext[i]) >= 'a' && tolower(plaintext[i]) <= 'z')
        {

            ascii = plaintext[i] + key;

            if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')
            {
                if (ascii > 90)
                {
                    cipher = ascii - 90 + 64;
                }
                else
                {
                    cipher = ascii;
                }
            }

            if (plaintext[i] >= 'a' && plaintext[i] <= 'z')
            {
                if (ascii > 122)
                {
                    cipher = ascii - 122 + 96;
                }
                else
                {
                    cipher = ascii;
                }
            }
        }
        else
        {
            cipher = plaintext[i];
        }

        printf("%c", cipher);
    }

    printf("\n");
}
