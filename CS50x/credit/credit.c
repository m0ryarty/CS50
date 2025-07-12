#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int validator = 0;
    int first_numbers;
    int second_numbers;
    long number = get_long("Your credit card numberd: ");

    do
    {
    first_numbers = number % 10;
    number = number / 10;
    second_numbers = number % 10;
    if((second_numbers *2) > 9){
        second_numbers = (second_numbers%10) + 1;
    }
    number = number / 10;
    validator = (first_numbers + (second_numbers *2) + validator) % 10;
    }
    while (number >= 1);

    

    printf("%i\n", first_numbers);
    printf("%i\n", second_numbers);



    printf("%i\n", validator);
}
