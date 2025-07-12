#include "stdio.h"
#include <math.h>


void main()
{
    int height = 0;
    int width = 1;

    int image[1][2];

    image[0][0] = 255;
    image[0][1] = 0;

    int leftR;
    int leftG;
    int leftB;
    int rightR;
    int rightG;
    int rightB;

    for (int i = 0; i < height; i++)
    {
       int k = width;
        for (int j = 0 ; j < (width/2); j++)
        {

            leftR = image[i][j].rgbtRed;
            leftG = image[i][j].rgbtGreen;
            leftB = image[i][j].rgbtBlue;
            rightR = image[i][k].rgbtRed;
            rightG = image[i][k].rgbtGreen;
            rightB = image[i][k].rgbtBlue;

            // Swap pixels
           int tmpRed = leftR;
           int tmpGreen = leftG;
           int tmpBlue = leftB;

           image[i][j].rgbtRed = rightR;
           image[i][j].rgbtGreen = rightG;
           image[i][j].rgbtBlue = rightB;

            image[i][k].rgbtRed = tmpRed;
            image[i][k].rgbtGreen = tmpGreen;
            image[i][k].rgbtBlue = tmpBlue;



            k--;

        }
    }
    return;
}
