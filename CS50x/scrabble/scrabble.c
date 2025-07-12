#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    int points(char letter);

    int points1 = 0;
    int points2 = 0;

    for (int i = 0, n = strlen(p1); i < n; i++)
    {
        char wp1 = tolower(p1[i]);

        points1 = points(wp1) + points1;
    }

    for (int i = 0, n = strlen(p2); i < n; i++)
    {
        char wp2 = tolower(p2[i]);

        points2 = points(wp2) + points2;
    }

    if (points1 > points2)
    {
        printf("Player 1 wins!\n");
    }
    else if (points2 > points1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int points(char letter)
{
    int p = 0;
    if (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'l' || letter == 'o' ||
        letter == 'r' || letter == 's' || letter == 't' || letter == 'u' || letter == 'n')
    {
        p = 1;
        return p;
    }
    else if (letter == 'd' || letter == 'g')
    {
        p = 2;
        return p;
    }
    else if (letter == 'b' || letter == 'c' || letter == 'm' || letter == 'p')
    {
        p = 3;
        return p;
    }
    else if (letter == 'f' || letter == 'h' || letter == 'v' || letter == 'w' || letter == 'y')
    {
        p = 4;
        return p;
    }
    else if (letter == 'k')
    {
        p = 5;
        return p;
    }
    else if (letter == 'j' || letter == 'x')
    {
        p = 8;
        return p;
    }
    else if (letter == 'q' || letter == 'z')
    {
        p = 10;
        return p;
    }
    else
    {
        p = 0;
        return p;
    }

    return p;
}
