#include <cs50.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK 512

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");

    // Create a buffer for a block of data
    uint8_t buffer[BLOCK];

    // While there's still data left to read from the memory card
    string filename = "000";
    int n = 0;
    FILE *file = NULL;
    while (fread(buffer, 1, BLOCK, card) == BLOCK)
    {

        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) &&
            ((buffer[3] & 0xf0) == 0xe0))
        {
            filename = malloc(3 * sizeof(int));
            if (n == 0)
            {
                sprintf(filename, "%03i.jpg", n);

                file = fopen(filename, "w");

                fwrite(buffer, 1, BLOCK, file);

                n++;
            }
            else
            {
                fclose(file);
                sprintf(filename, "%03i.jpg", n);

                file = fopen(filename, "w");

                fwrite(buffer, 1, BLOCK, file);

                n++;
            }

            free(filename);
        }
        else
        {
            if (file)
            {
                fwrite(buffer, 1, BLOCK, file);
            }
        }

        // Create JPEGs from the data
    }
    fclose(file);
    fclose(card);
}
