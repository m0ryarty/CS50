#include "helpers.h"
#include "stdio.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            double avg = (image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0;

            image[i][j].rgbtBlue = (int) round(avg);
            image[i][j].rgbtRed = (int) round(avg);
            image[i][j].rgbtGreen = (int) round(avg);
        }
    }

    return;
}

// Convert image to sepia
int *pixelSepia(int red, int green, int blue);

int rpixel;
int gpixel;
int bpixel;

void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            rpixel =
                pixelSepia(image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue)[0];
            gpixel =
                pixelSepia(image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue)[1];
            bpixel =
                pixelSepia(image[i][j].rgbtRed, image[i][j].rgbtGreen, image[i][j].rgbtBlue)[2];

            image[i][j].rgbtRed = rpixel;
            image[i][j].rgbtGreen = gpixel;
            image[i][j].rgbtBlue = bpixel;
        }
    }
    return;
}

int *pixelSepia(red, green, blue)
{
    static int pixel[3];

    int rsepia = round(.393 * red + .769 * green + .189 * blue);

    if (rsepia > 255)

    {
        rsepia = 255;
    }

    pixel[0] = rsepia;

    int gsepia = round(.349 * red + .686 * green + .168 * blue);

    if (gsepia > 255)

    {
        gsepia = 255;
    }

    pixel[1] = gsepia;

    int bsepia = round(.272 * red + .534 * green + .131 * blue);

    if (bsepia > 255)

    {
        bsepia = 255;
    }

    pixel[2] = bsepia;

    return pixel;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    // Loop over all pixels

    RGBTRIPLE tmp;
    RGBTRIPLE *left;
    RGBTRIPLE *right;

    for (int i = 0; i < height; i++)
    {
        int k = width - 1;
        for (int j = 0; j < (width / 2); j++)
        {
            // Swap pixels
            left = &image[i][j];
            right = &image[i][k];

            tmp = *right;

            *right = *left;

            *left = tmp;

            k--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            double avgRed;
            double avgGreen;
            double avgBlue;

            avgRed =
                (copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed +
                 copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed +
                 copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed) /
                9.0;
            avgGreen =
                (copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen +
                 copy[i - 1][j + 1].rgbtGreen + copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen +
                 copy[i][j + 1].rgbtGreen + copy[i + 1][j - 1].rgbtGreen +
                 copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) /
                9.0;
            avgBlue = (copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue +
                       copy[i - 1][j + 1].rgbtBlue + copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue +
                       copy[i][j + 1].rgbtBlue + copy[i + 1][j - 1].rgbtBlue +
                       copy[i + 1][j].rgbtBlue + copy[i + 1][j + 1].rgbtBlue) /
                      9.0;

            if (i == 0)
            {
                avgRed = (copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed +
                          copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed +
                          copy[i + 1][j + 1].rgbtRed) /
                         6.0;
                avgGreen = (copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen +
                            copy[i][j + 1].rgbtGreen + copy[i + 1][j - 1].rgbtGreen +
                            copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) /
                           6.0;
                avgBlue = (copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue +
                           copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue +
                           copy[i + 1][j + 1].rgbtBlue) /
                          6.0;
            }

            if (i == height - 1)
            {
                avgRed = (copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed +
                          copy[i - 1][j + 1].rgbtRed + copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed +
                          copy[i][j + 1].rgbtRed) /
                         6.0;
                avgGreen = (copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen +
                            copy[i - 1][j + 1].rgbtGreen + copy[i][j - 1].rgbtGreen +
                            copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen) /
                           6.0;
                avgBlue = (copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue +
                           copy[i - 1][j + 1].rgbtBlue + copy[i][j - 1].rgbtBlue +
                           copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue) /
                          6.0;
            }

            if (j == 0)
            {
                avgRed =
                    (copy[i - 1][j].rgbtRed + copy[i - 1][j + 1].rgbtRed + copy[i][j].rgbtRed +
                     copy[i][j + 1].rgbtRed + copy[i + 1][j].rgbtRed + copy[i + 1][j + 1].rgbtRed) /
                    6.0;
                avgGreen = (copy[i - 1][j].rgbtGreen + copy[i - 1][j + 1].rgbtGreen +
                            copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen +
                            copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) /
                           6.0;
                avgBlue = (copy[i - 1][j].rgbtBlue + copy[i - 1][j + 1].rgbtBlue +
                           copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i + 1][j].rgbtBlue +
                           copy[i + 1][j + 1].rgbtBlue) /
                          6.0;
            }

            if (j == width - 1)
            {
                avgRed =
                    (copy[i - 1][j - 1].rgbtRed + copy[i - 1][j].rgbtRed + copy[i][j - 1].rgbtRed +
                     copy[i][j].rgbtRed + copy[i + 1][j - 1].rgbtRed + copy[i + 1][j].rgbtRed) /
                    6.0;
                avgGreen = (copy[i - 1][j - 1].rgbtGreen + copy[i - 1][j].rgbtGreen +
                            copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen +
                            copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen) /
                           6.0;
                avgBlue = (copy[i - 1][j - 1].rgbtBlue + copy[i - 1][j].rgbtBlue +
                           copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue +
                           copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue) /
                          6.0;
            }

            if (i == 0 && j == 0)
            {
                avgRed = (copy[i][j].rgbtRed + copy[i][j + 1].rgbtRed + copy[i + 1][j].rgbtRed +
                          copy[i + 1][j + 1].rgbtRed) /
                         4;
                avgGreen = (copy[i][j].rgbtGreen + copy[i][j + 1].rgbtGreen +
                            copy[i + 1][j].rgbtGreen + copy[i + 1][j + 1].rgbtGreen) /
                           4;
                avgBlue = (copy[i][j].rgbtBlue + copy[i][j + 1].rgbtBlue + copy[i + 1][j].rgbtBlue +
                           copy[i + 1][j + 1].rgbtBlue) /
                          4;
            }

            if (i == 0 && (j == width - 1))
            {
                avgRed = (copy[i][j - 1].rgbtRed + copy[i][j].rgbtRed + copy[i + 1][j - 1].rgbtRed +
                          copy[i + 1][j].rgbtRed) /
                         4.0;
                avgGreen = (copy[i][j - 1].rgbtGreen + copy[i][j].rgbtGreen +
                            copy[i + 1][j - 1].rgbtGreen + copy[i + 1][j].rgbtGreen) /
                           4.0;
                avgBlue = (copy[i][j - 1].rgbtBlue + copy[i][j].rgbtBlue +
                           copy[i + 1][j - 1].rgbtBlue + copy[i + 1][j].rgbtBlue) /
                          4.0;
            }

            if (i == (height - 1) && (j == 0))
            {
                avgRed = (copy[i - 1][j].rgbtRed + copy[i][j].rgbtRed + copy[i - 1][j + 1].rgbtRed +
                          copy[i][j + 1].rgbtRed) /
                         4.0;
                avgGreen = (copy[i - 1][j].rgbtGreen + copy[i][j].rgbtGreen +
                            copy[i - 1][j + 1].rgbtGreen + copy[i][j + 1].rgbtGreen) /
                           4.0;
                avgBlue = (copy[i - 1][j].rgbtBlue + copy[i][j].rgbtBlue +
                           copy[i - 1][j + 1].rgbtBlue + copy[i][j + 1].rgbtBlue) /
                          4.0;
            }

            if (i == (height - 1) && (j == width - 1))
            {
                avgRed = (copy[i - 1][j].rgbtRed + copy[i][j].rgbtRed + copy[i - 1][j - 1].rgbtRed +
                          copy[i][j - 1].rgbtRed) /
                         4.0;
                avgGreen = (copy[i - 1][j].rgbtGreen + copy[i][j].rgbtGreen +
                            copy[i - 1][j - 1].rgbtGreen + copy[i][j - 1].rgbtGreen) /
                           4.0;
                avgBlue = (copy[i - 1][j].rgbtBlue + copy[i][j].rgbtBlue +
                           copy[i - 1][j - 1].rgbtBlue + copy[i][j - 1].rgbtBlue) /
                          4.0;
            }

            image[i][j].rgbtRed = (int) round(avgRed);
            image[i][j].rgbtGreen = (int) round(avgGreen);
            image[i][j].rgbtBlue = (int) round(avgBlue);
        }
    }

    return;
}
