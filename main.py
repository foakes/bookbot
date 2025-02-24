import sys

from stats import get_wordcount
from stats import get_char_count
from stats import generate_report_values

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    full_text = get_book_text(book)
    word_count = get_wordcount(full_text)
    #print(f"{word_count} words found in the document")
    char_count = get_char_count(full_text)
    #print(char_count)
    sorted_list = generate_report_values(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(sorted_list)):
        for k, v in sorted_list[i].items():
            if k.isalpha() == True:
                print(f"{k}: {v}")
    print("============= END ===============")

main()
    