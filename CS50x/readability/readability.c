#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string text = get_string("Text: ");

    float w = 1;
    float l = 0;
    float s = 0;
    float letter_average = 0;
    float sentence_average = 0;
    float index = 0;

    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == ' ')
        {
            w++;
        }

        else if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            s++;
        }

        else if (tolower(text[i]) >= 'a' && tolower(text[i]) <= 'z')
        {
            l++;
        }
    }

    sentence_average = ((s / w) * 100);
    letter_average = (((l) / w) * 100);

    index = 0.0588 * letter_average - 0.296 * sentence_average - 15.8;

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(index));
    }
}
