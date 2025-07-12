// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26 * 26 * 26 * 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    int index = hash(word);

    for (node *ptr = table[index]; ptr != NULL; ptr = ptr->next)
    {
        if (strcasecmp(word, ptr->word) == 0)
        {
            return true;
        }
    }

    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int hashIdx = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        hashIdx = hashIdx + toupper(word[i]);
    }

    // TODO: Improve this hash function
    return hashIdx;
}

int wordCount = 0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    char word[LENGTH + 1];

    FILE *source = fopen(dictionary, "r");

    if (source != NULL)
    {

        fscanf(source, "%s", word);
        do
        {

            node *n = malloc(sizeof(node));

            if (n == NULL)
            {
                return false;
            }

            strcpy(n->word, word);
            n->next = NULL;

            int index = hash(word);

            if (table[index] == NULL)
            {
                table[index] = n;
            }
            else
            {
                for (node *ptr = table[index]; ptr != NULL; ptr = ptr->next)
                {
                    if (ptr->next == NULL)
                    {
                        ptr->next = n;
                        break;
                    }
                }
            }
        }
        while (fscanf(source, "%s", word) != EOF);

        for (int i = 0; i < N; i++)
        {

            for (node *ptr = table[i]; ptr != NULL; ptr = ptr->next)
            {
                wordCount++;
            }
        }

        fclose(source);

        return true;
    }

    fclose(source);
    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{

    return wordCount;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{

    for (int i = 0; i < N; i++)
    {

        node *ptr = table[i];
        while (ptr != NULL)
        {
            node *next = ptr->next;
            free(ptr);
            ptr = next;
        }
    }

    return true;
}
