#include <cs50.h>
#include <stdio.h>
#include <strings.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();

        bool tie = is_tie(min);

        printf("min: %i\n", min);

        // If tie, everyone wins
        if (tie)
        {
            printf("empatado\n");
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{

    for (int i = 0; i < candidate_count; i++)
    {
        if (strcasecmp(name, candidates[i].name) == 0)
        {
            preferences[voter][rank] = i;

            return true;
        }
    }

    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{

    for (int i = 0; i < voter_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (candidates[preferences[i][j]].eliminated == false)
            {
                candidates[preferences[i][j]].votes++;
                break;
            }
        }
    }

    printf("%s: %i\n", candidates[0].name, candidates[0].votes);
    printf("%s: %i\n", candidates[1].name, candidates[1].votes);
    printf("%s: %i\n", candidates[2].name, candidates[2].votes);
    printf("%s: %i\n", candidates[3].name, candidates[3].votes);

    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    for (int i = voter_count; i > 0; i--)
    {

        for (int j = 0; j < voter_count; j++)
        {

            if (candidates[j].votes == i && candidates[j].votes > (voter_count / 2))
            {

                printf("winner: %s\n", candidates[j].name);

                return true;
            }
        }
    }
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    int m = 0;
    for (int i = 0; i < candidate_count; i++)
    {

        if (candidates[i].votes < voter_count && candidates[i].eliminated == false)
        {

            if (candidates[i].votes < candidates[i - 1].votes)
            {
                m = candidates[i].votes;
            }
            else
            {
                m = candidates[i - 1].votes;
            }
        }
    }

    if (m > 0)
    {
        return m;
    }

    return 0;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{

    int t = 0;
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].eliminated == false)
        {

            if (candidates[i + 1].votes != 0)
            {
                if (candidates[i].votes != candidates[i + 1].votes)
                {
                    printf("pv: %i\n", candidates[i + 1].votes);
                    return false;
                }
                else
                {
                    t = 1;
                }
            }
        }
    }

    if (t == 1)
    {
        printf("tieded");
        return true;
    }

    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{

    for (int i = 0; i < voter_count; i++)
    {
        if (candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }

    return;
}
