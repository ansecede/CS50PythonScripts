# Task description: https://cs50.harvard.edu/x/2022/psets/6/readability/


from cs50 import get_string
import sys
# TODO


def main():
    # Variables
    text = get_string("Text: ")
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Checking if the text has no words
    if (words == 0):
        printf("The text you inserted has no words. Exiting...")
        sys.exit(1)

    # Now that we know that the text has at least a word, we calculate the Coleman-Liau index
    L = float(letters) / words * 100.00
    S = float(sentences) / words * 100.00
    index = 0.0588 * L - 0.296 * S - 15.8

    # Index number is 16 or higher, output  "Grade 16+"
    if index > 16:
        print("Grade 16+")
        sys.exit(0)
    # If the index number is less than 1, output "Before Grade 1".
    if index < 1:
        print("Before Grade 1")
        sys.exit(0)

    print(f"Grade {round(index)}")
    sys.exit(0)


# Function to count letters
def count_letters(text):
    num_letters = 0

    for char in text:
        if char.isalpha():
            num_letters += 1

    return num_letters


# Function to count words
def count_words(text):
    num_words = 0
    length = len(text)

    # Making sure the text has at least a character, which means a word.
    if length == 0:
        return 0

    for i in range(length):
        if (text[i] == " ") and (text[i - 1] != " "):
            num_words += 1

    return num_words + 1


# Function to count sentences
def count_sentences(text):
    num_sentences = 0

    for char in text:
        if (char == ".") or (char == "!") or (char == "?"):
            num_sentences += 1

    return num_sentences


if __name__ == "__main__":
    main()