import csv
import sys

argv = sys.argv


def main():

    # TODO: Check for command-line usage

    if (len(argv) < 3):
        print('Not enough arguments')

    # TODO: Read database file into a variable

    people = []
    with open(argv[1]) as file:
        reader = csv.DictReader(file)
        for person in reader:
            people.append(person)
        subsequence = reader.fieldnames
        subsequence.pop(0)

    # TODO: Read DNA sequence file into a variable

    sequence = open(argv[2]).read()

    # TODO: Find longest match of each STR in DNA sequence

    matches = {}

    for i in subsequence:
        tm = str(longest_match(sequence, i))
        tmDic = {i: tm}
        matches.update(tmDic)

    # TODO: Check database for matching profiles

    for i in people:
        name = i.pop('name')

        if (i == matches):
            print(name)
            return

    print('No match')
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
