import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)


def main():
    """ Read in lines from a file """

    # Open the dictionary for reading
    my_file = open("dictionary.txt")

    # Create an empty list to store the words
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    my_file.close()

    print("--- Linear Search ---")

    #Open the text for reading
    my_book = open("AliceInWonderLand200.txt")

    line_number = 0

    for line in my_book:
        word_list = split_line(line)
        line_number += 1

        for word in word_list:

            key = word.upper()
            current_list_position = 0

            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:
                current_list_position += 1

            if current_list_position >= len(dictionary_list):
                print("line", line_number, word)

    my_book.close()

    print("--- Binary Search ---")

    # Open the text for reading
    my_book = open("AliceInWonderLand200.txt")


    line_number = 0

    for line in my_book:
        word_list = split_line(line)
        line_number += 1

        for word in word_list:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            # Loop until we find the item, or our upper/lower bounds meet
            while lower_bound <= upper_bound and not found:

                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

            if not found:
                print("line", line_number, word)

main()